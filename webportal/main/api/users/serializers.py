from rest_framework import serializers

from main.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ['room', 'passport', 'checkout_date', 'token']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
