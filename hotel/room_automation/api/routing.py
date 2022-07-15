from django.urls import path

from .api import consumers

websocket_urlpatterns = [
    path(r'ws/room/', consumers.RoomAutomationConsumer.as_asgi())
]
