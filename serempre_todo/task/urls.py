from django.urls import path

from serempre_todo.task.views import (
    task_create_view,
    task_time_worked_update_view,
    task_update_view,
)

app_name = "task"
urlpatterns = [
    path("create/", view=task_create_view, name="task-create"),
    path("<str:pk>/", view=task_update_view, name="task-update"),
    path("time-worked/<str:pk>/", view=task_time_worked_update_view, name="task-time-worked-update-view"),
]
