from django.urls import path

from main.views import AuthorizationView, IndexView
from main.views.authorization import logout_view

urlpatterns = [
    path('authorization/', AuthorizationView.as_view(), name='authorization'),
    path('logout/', logout_view, name='logout'),
    path('', IndexView.as_view(), name='home'),
]
