import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MedicalSchedulingConfig(AppConfig):
    name = "healthcare_app_api.medical_scheduling"
    verbose_name = _("Medical Scheduling")

    def ready(self):
        with contextlib.suppress(ImportError):
            import healthcare_app_api.medical_scheduling.signals  # noqa: F401
