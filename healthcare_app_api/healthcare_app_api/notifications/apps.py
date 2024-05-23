import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class NotificationsConfig(AppConfig):
    name = "healthcare_app_api.notifications"
    verbose_name = _("Notifications")

    def ready(self):
        with contextlib.suppress(ImportError):
            import healthcare_app_api.medical_scheduling.signals  # noqa: F401
