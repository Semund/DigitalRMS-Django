from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from room_automation.api.serializers import RoomAutomationSerializer
from room_automation.models import RoomAutomation


class RoomAutomationViewSet(GenericViewSet, RetrieveModelMixin, UpdateModelMixin):
    queryset = RoomAutomation.objects.all()
    lookup_field = 'number'
    serializer_class = RoomAutomationSerializer

