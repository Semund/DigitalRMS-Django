from django.urls import path, include
from rest_framework.routers import DefaultRouter

from room_automation.api.endpoints import RoomAutomationViewSet
from room_automation.views import room_view

api_router = DefaultRouter()
api_router.register(r'rooms', RoomAutomationViewSet)
print(api_router.urls)

urlpatterns = [
    path('', room_view, name='room'),
    path('api/v1/', include(api_router.urls))
]
