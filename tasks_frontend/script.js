const API_BASE = "http://127.0.0.1:8000/api";

// ---------- AUTH ----------

function register() {
  fetch(`${API_BASE}/auth/v1/register/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      username: document.getElementById("reg-username").value,
      email: document.getElementById("reg-email").value,
      password: document.getElementById("reg-password").value,
    }),
  })
    .then(res => res.json())
    .then(() => {
      document.getElementById("message").innerText = "Registered successfully";
    });
}

function login() {
  fetch(`${API_BASE}/auth/v1/login/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      username: document.getElementById("login-username").value,
      password: document.getElementById("login-password").value,
    }),
  })
    .then(res => res.json())
    .then(data => {
      localStorage.setItem("access", data.access);
      window.location.href = "dashboard.html";
    });
}

function logout() {
  localStorage.removeItem("access");
  window.location.href = "index.html";
}

// ---------- HELPERS ----------

function authHeaders() {
  return {
    "Content-Type": "application/json",
    "Authorization": `Bearer ${localStorage.getItem("access")}`,
  };
}

// ---------- TASKS ----------

function loadTasks() {
  fetch(`${API_BASE}/tasks/v1/task_create_list/`, {
    headers: authHeaders(),
  })
    .then(res => {
      if (!res.ok) {
        throw new Error("Unauthorized or failed request");
      }
      return res.json();
    })
    .then(data => {
      if (!Array.isArray(data)) {
        console.error("Expected array, got:", data);
        return;
      }

      const list = document.getElementById("task-list");
      list.innerHTML = "";

      data.forEach(task => {
        const li = document.createElement("li");
        li.innerText = `${task.title} (${task.status})`;

        const delBtn = document.createElement("button");
        delBtn.innerText = "Delete";
        delBtn.onclick = () => deleteTask(task.id);

        li.appendChild(delBtn);
        list.appendChild(li);
      });
    })
    .catch(err => {
      console.error(err);
      alert("Session expired or unauthorized. Please log in again.");
      logout();
    });
}


function createTask() {
  fetch(`${API_BASE}/tasks/v1/task_create_list/`, {
    method: "POST",
    headers: authHeaders(),
    body: JSON.stringify({
      title: document.getElementById("task-title").value,
      description: document.getElementById("task-desc").value,
      status: "todo",
    }),
  }).then(() => loadTasks());
}

function deleteTask(id) {
  fetch(`${API_BASE}/tasks/v1/task_detail/${id}`, {
    method: "DELETE",
    headers: authHeaders(),
  }).then(() => loadTasks());
}

// Auto-load tasks on dashboard
if (window.location.pathname.includes("dashboard")) {
  loadTasks();
}
