from django.urls import path

from registration import views
from registration.api.guest.endpoints import GuestAPIView

urlpatterns = [
    path('', views.CheckinView.as_view(), name='checkin'),
    path('api/v1/guest', GuestAPIView.as_view())
]