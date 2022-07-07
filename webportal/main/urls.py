from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from main.api.guest_data.endpoints import GuestDataAPIView
from main.api.users.endpoints import RegistrationAPIView
from main.views import authorization, index

urlpatterns = [
    path('authorization/', authorization, name='authorization'),
    path('', index, name='home'),
    path('api/v1/guest/', GuestDataAPIView.as_view(), name='guest_api'),
    path('api/v1/users/', RegistrationAPIView.as_view(), name='registration'),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]