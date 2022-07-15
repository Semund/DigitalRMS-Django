from rest_framework import serializers

from registration.models import Guest, Booking


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ('first_name',)


class GuestDataSerializer(serializers.ModelSerializer):
    guests = GuestSerializer(many=True, read_only=True)
    room = serializers.CharField(source='room.number')

    class Meta:
        model = Booking
        fields = ('guests', 'room', 'checkin_date', 'checkout_date')
