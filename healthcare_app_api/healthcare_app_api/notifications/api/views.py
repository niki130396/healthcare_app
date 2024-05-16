from os import environ

import aiohttp
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from healthcare_app_api.healthcare_app_api.medical_scheduling.models import (
    Customer,
)
from healthcare_app_api.healthcare_app_api.notifications.models import (
    Notification,
)
from healthcare_app_api.healthcare_app_api.notifications.api.serializers import (
    NotificationSerializer,
)


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    @action(detail=True, methods=["POST"])
    def send_sms_notifications_bulk(self, request, *args, **kwargs):
        account_sid = environ.get("TWILIO_ACCOUNT_SID")
        auth_token = environ.get("TWILIO_AUTH_TOKEN")
        twilio_phone_number = environ.get("TWILIO_PHONE_NUMBER")
        serializer = NotificationSerializer(data=request.data)
        if serializer.is_valid():

            customer_ids = request.data.get("customers")
            customers = Customer.objects.filter(pk__in=customer_ids)
            sms_body = request.data.get("message")
            auth = aiohttp.BasicAuth(login=account_sid, password=auth_token)
            async with aiohttp.ClientSession(auth=auth) as session:
                for customer in customers:
                    return await session.post(
                        f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages.json",
                        data={"From": twilio_phone_number, "To": customer.contact_mobile, "Body": sms_body}
                    )
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
