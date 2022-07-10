from django.urls import path

from main.views import AuthorizationView, IndexView

urlpatterns = [
    path('authorization/', AuthorizationView.as_view(), name='authorization'),
    path('', IndexView.as_view(), name='home'),
]
