from django.urls import path

from room_automation.views import room_view

urlpatterns = [
    path('', room_view, name='room'),
]