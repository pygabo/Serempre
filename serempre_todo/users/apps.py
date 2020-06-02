from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "serempre_todo.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import serempre_todo.users.signals  # noqa F401
        except ImportError:
            pass
