from django import forms

from room_automation.models import RoomAutomation


class RoomAutomationForm(forms.Form):
    number = forms.ModelChoiceField(
                empty_label='Номер не выбран',
                label='Выберите номер:',
                queryset=RoomAutomation.objects.all(),
                widget=forms.Select(attrs={'class': 'form-control submit',
                                           'type': 'text',
                                           'onchange': 'getRoomData(this.value);'})
            )
