from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status

from .serializers import TaskSerializer
from .models import Task

from rest_framework.views import APIView

from django.shortcuts import get_object_or_404

from .permission import IsOwnerOrAdmin

"""
view to handle:
task creatation by the user
the list (get) all tasks created by the user
user must be authorized to perform any action, need access JWT
"""
class TaskListCreateView(APIView):
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
    serializer_class = TaskSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by = request.user)
            return Response(
                {
                    "message": "Task Created",
                    "task": serializer.data
                },
                status=status.HTTP_201_CREATED
            )
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        if request.user.is_staff or request.user.is_superuser:
            tasks = Task.objects.all()
        else:
            tasks = Task.objects.filter(created_by=request.user)

        serializer = self.serializer_class(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
"""
view to handle individual task operations
get
put
delete
"""
class TaskDetailView(APIView):
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
    serializer_class = TaskSerializer

    def get_object(self, pk):
        return get_object_or_404(Task, pk=pk)

    def get(self, request, pk):
        task = self.get_object(pk)
        self.check_object_permissions(request, task)
        serializer = self.serializer_class(task)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        task = self.get_object(pk)
        self.check_object_permissions(request, task)

        serializer = self.serializer_class(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = self.get_object(pk)
        self.check_object_permissions(request, task)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
