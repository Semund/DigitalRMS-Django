from django.urls import path

from authorization.views import AuthorizationView, logout_view

urlpatterns = [
    path('', AuthorizationView.as_view(), name='authorization'),
    path('logout/', logout_view, name='logout'),
]
