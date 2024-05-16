from rest_framework import serializers


from healthcare_app_api.healthcare_app_api.medical_scheduling.models import (
    Customer,
)
from healthcare_app_api.healthcare_app_api.notifications.models import (
    Notification,
)


class NotificationSerializer(serializers.ModelSerializer):
    customers = serializers.PrimaryKeyRelatedField(many=True, queryset=Customer.objects.all())

    class Meta:
        model = Notification
        fields = "__all__"

    def create(self, validated_data):
        customers_data = validated_data.pop("customers")
        notifications = []
        for customer in customers_data:
            notifications.append(
                Notification(**validated_data, customer=customer)
            )
        Notification.objects.bulk_create(notifications)
