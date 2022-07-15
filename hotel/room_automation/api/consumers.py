from djangochannelsrestframework import permissions
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.mixins import UpdateModelMixin
from djangochannelsrestframework.observer.generics import ObserverModelInstanceMixin

from room_automation.api.serializers import RoomAutomationSerializer
from room_automation.models import RoomAutomation


class RoomAutomationConsumer(ObserverModelInstanceMixin, GenericAsyncAPIConsumer, UpdateModelMixin):
    queryset = RoomAutomation.objects.all()
    serializer_class = RoomAutomationSerializer
    permission_classes = (permissions.AllowAny,)
