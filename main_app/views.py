from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from datetime import timedelta

from .models import Asset, Notification, Violation
from .serializers import AssetSerializer

class AssetView(APIView):
    def get(self, request):
        assets = Asset.objects.all()
        return Response(AssetSerializer(assets, many=True).data)

    def post(self, request):
        serializer = AssetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RunChecksView(APIView):
    def get(self, request):
        now = timezone.now()
        fifteen_min_later = now + timedelta(minutes=15)
        notifications = []
        violations = []

        assets = Asset.objects.all()
        for asset in assets:
            # Reminder 15 min before service or expiration
            if now <= asset.service_time <= fifteen_min_later:
                msg = f"Service time approaching for {asset.name}"
                Notification.objects.create(asset=asset, message=msg)
                notifications.append(msg)
            if now <= asset.expiration_time <= fifteen_min_later:
                msg = f"Expiration time approaching for {asset.name}"
                Notification.objects.create(asset=asset, message=msg)
                notifications.append(msg)
  
            # Violation Check
            if now > asset.service_time and not asset.is_serviced:
                reason = f"Asset {asset.name} missed service time"
                Violation.objects.get_or_create(asset=asset, reason=reason)
                violations.append(reason)
            if now > asset.expiration_time:
                reason = f"Asset {asset.name} expired"
                Violation.objects.get_or_create(asset=asset, reason=reason)
                violations.append(reason)

        return Response({
            "notifications_created": notifications,
            "violations_created": violations
        }, status=200)
