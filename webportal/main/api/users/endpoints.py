from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from main.api.users.renderers import UserJSONRenderer
from main.api.users.serializers import RegistrationSerializer, LoginSerializer


class RegistrationAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        user = {
            'room': request.data.get('room', None),
            'passport': request.data.get('passport', None),
            'checkout_date': request.data.get('checkout_date', None)
        }
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        user = {
            'room': request.data.get('room', None),
            'passport': request.data.get('passport', None),
        }

        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
