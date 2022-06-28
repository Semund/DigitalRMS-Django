from django import forms

from registration.models import Room
from room_automation.models import RoomAutomation


class RoomAutomationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['room'].empty_label = 'Номер не выбран'

    class Meta:
        model = RoomAutomation
        fields = ('room',)
        widgets = {
            'room': forms.Select(attrs={'class': 'form-control submit', 'type': 'text'}, choices=tuple(Room.objects.all(

            ))),
        }
