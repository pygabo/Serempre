# Rest Framework
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
# Model
from serempre_todo.task.models import Task

# Serializer
from serempre_todo.task.api.serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [AllowAny]
    queryset = Task.objects.all()
