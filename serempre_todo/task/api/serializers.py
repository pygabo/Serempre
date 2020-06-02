from rest_framework import serializers

# Model
from serempre_todo.task.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            'id',
            'title',
            'description',
            'estimated_time',
            'time_worked',
            'status',
            'assignee',
            'reporter',
            'priority',
        )
        read_only_fields = (
            'id',
        )
