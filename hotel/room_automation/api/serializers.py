from rest_framework import serializers


from room_automation.models import RoomAutomation


class RoomAutomationSerializer(serializers.ModelSerializer):
   class Meta:
        model = RoomAutomation
        fields = ('number', 'light', 'climat')
