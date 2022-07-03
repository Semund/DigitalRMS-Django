from rest_framework.generics import RetrieveAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from room_automation.api.serializers import RoomAutomationSerializer
from room_automation.models import RoomAutomation


class RoomAutomationViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = RoomAutomation.objects.all()
    serializer_class = RoomAutomationSerializer
    # permission_classes = (AllowAny,)