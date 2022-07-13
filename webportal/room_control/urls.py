from django.urls import path

from room_control.views import RoomControlView

urlpatterns = [
    path('', RoomControlView.as_view(), name='room_control'),
]