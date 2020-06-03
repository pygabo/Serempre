from django.forms import ModelForm

# Model
from serempre_todo.task.models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = (
            'title',
            'description',
            'estimated_time',
            'status',
            'assignee',
            'reporter',
            'priority',
        )


class TaskTimeWorkedForm(ModelForm):
    class Meta:
        model = Task
        fields = (
            'time_worked',
        )
