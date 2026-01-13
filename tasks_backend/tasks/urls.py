from django.urls import path
from . import views

urlpatterns = [
    path('v1/task_create_list/', view=views.TaskListCreateView.as_view(), name='task-create-list'),
    path('v1/task_detail/<int:pk>', view=views.TaskDetailView.as_view(), name='task-detail'),
]