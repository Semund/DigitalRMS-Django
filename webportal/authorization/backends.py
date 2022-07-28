from django.contrib.auth.backends import BaseBackend

from authorization.models import User


class AuthenticationWithoutPassword(BaseBackend):

    def authenticate(self, request, passport=None, room=None):
        if passport is None and room is None:
            passport = request.data.get('passport', '')
            room = request.data.get('room', '')
        try:
            return User.objects.get(passport=passport, room=room)
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
