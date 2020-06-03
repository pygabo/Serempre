from django.conf import settings
from django.db import models

from serempre_todo.utils.choices import TASK_PRIORITY, TASK_STATUS
# Utils
from serempre_todo.utils.models import BaseModel


class Task(BaseModel):
    title = models.CharField(max_length=32)
    description = models.TextField()
    estimated_time = models.PositiveSmallIntegerField()
    time_worked = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=2, choices=TASK_STATUS, default=TASK_STATUS[0][0])
    assignee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='assignee')
    reporter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reporter')
    priority = models.CharField(max_length=2, choices=TASK_PRIORITY, default=TASK_PRIORITY[0][0])

    def remaining_time(self):
        return self.estimated_time - self.time_worked

    def __str__(self):
        return self.title
