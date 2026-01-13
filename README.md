# Backend Developer Intern Assignment – Task Management API

## Overview
This project is a backend-focused REST API with JWT authentication, role-based access control,
and a basic frontend to demonstrate API functionality.

## Tech Stack
- Backend: Django, Django REST Framework
- Auth: JWT (SimpleJWT)
- Database: SQLite (development)
- API Docs: Swagger (drf-spectacular)
- Frontend: Vanilla JavaScript (supportive UI)

## Features

### Authentication
- User registration with password hashing
- User login with JWT access & refresh tokens

### Role-Based Access Control
- Normal users: manage their own tasks
- Admin users: can view and manage all tasks

### Task Management (CRUD)
- Create, list, update, delete tasks
- Ownership enforced at object level

### API Versioning
- APIs are versioned (v1) to allow future changes without breaking clients

### API Documentation
- Swagger UI available at `/api/docs/`

### Frontend (Supportive)
- Simple UI to:
  - Register & login users
  - Access protected dashboard
  - Perform CRUD operations on tasks
- Frontend communicates with backend using JWT

## Project Setup

### Backend
##### requirements.txt is in the tasks_backend folder
```bash
cd tasks_backend
python3 -m venv env
source /bin/env/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
### Frontend
#### MAKE SURE TO RUN FRONTEND ON SERVER
```bash
cd tasks_frontend
python3 -m http.server 5500
```

## Scalability Considerations

- The backend is structured in a modular way (accounts, tasks), so new features
  or services can be added easily. If the system grows, these modules can also
  be separated into individual services.

- JWT based authentication is stateless, which makes it easier to scale the
  application horizontally without worrying about shared session storage.

- Currently SQLite is used for development, but the database layer can be moved
  to PostgreSQL or MySQL when handling higher traffic and concurrent users.

- For frequently accessed data like task lists, caching solutions such as Redis
  can be introduced to reduce database load and improve response times.

- The application can be containerized using Docker and deployed behind a load
  balancer (for example Nginx) to handle increased traffic more reliably.

- Logging and basic monitoring can be added to better track errors, performance
  issues, and overall system health in a production environment.

