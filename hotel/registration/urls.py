from django.urls import path

from registration import views

urlpatterns = [
    path('', views.CheckinView.as_view(), name='checkin'),
]