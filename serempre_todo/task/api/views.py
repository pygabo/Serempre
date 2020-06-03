# Rest Framework
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Serializer
from serempre_todo.task.api.serializers import TaskSerializer
# Model
from serempre_todo.task.models import Task


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
