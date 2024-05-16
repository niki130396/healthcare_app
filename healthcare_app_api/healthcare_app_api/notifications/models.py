from django.db import models

from healthcare_app_api.healthcare_app_api.medical_scheduling.models import (
    Customer,
    Employee,
)


class Notification(models.Model):
    id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    message = models.TextField()
    sent_on = models.DateTimeField(auto_now_add=True)
    notification_channel = models.CharField(max_length=128)
