from django.contrib.auth import authenticate
from rest_framework import serializers

from main.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ['room', 'passport', 'checkout_date', 'token']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    passport = serializers.CharField(max_length=12)
    room = serializers.CharField(max_length=3)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        room = data.get('room', None)
        passport = data.get('passport', None)

        if room is None:
            raise serializers.ValidationError(
                'A room number is required to log in.'
            )

        if passport is None:
            raise serializers.ValidationError(
                'A passport data is required to log in.'
            )

        user = authenticate(passport=passport)

        if user is None:
            raise serializers.ValidationError(
                'A user with this passport and room number was not found.'
            )

        return {
            'passport': user.passport,
            'room': user.room,
            'token': user.token
        }
