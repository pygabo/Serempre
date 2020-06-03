from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

# Forms
from serempre_todo.task.forms import TaskForm, TaskTimeWorkedForm
# Model
from serempre_todo.task.models import Task


class TaskListView(ListView):
    model = Task
    context_object_name = 'task_list'


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('task-list')


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('task-list')


class TaskTimeWorkedUpdateView(UpdateView):
    model = Task
    form_class = TaskTimeWorkedForm
    success_url = reverse_lazy('task-list')


task_create_view = TaskCreateView.as_view()
task_list_view = TaskListView.as_view()
task_update_view = TaskUpdateView.as_view()
task_time_worked_update_view = TaskTimeWorkedUpdateView.as_view()
