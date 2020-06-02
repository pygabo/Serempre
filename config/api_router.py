from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from serempre_todo.users.api.views import UserViewSet
from serempre_todo.task.api.views import TaskViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("task", TaskViewSet)

app_name = "api"
urlpatterns = router.urls
