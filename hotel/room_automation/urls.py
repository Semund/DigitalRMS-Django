from django.urls import path

from room_automation.views import room_view, RoomAutomationView

urlpatterns = [
    path('', room_view, name='room'),
    path('test/', RoomAutomationView.as_view(), name='room_test')
]