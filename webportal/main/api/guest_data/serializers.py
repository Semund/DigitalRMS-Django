from rest_framework import serializers

from main.models import Guest


class GuestDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ('name', 'checkin_date', 'checkout_date', 'room')
