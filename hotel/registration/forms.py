from django import forms

from .models import Booking, Guest, Room


class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ('passport_number', 'date_of_issue', 'first_name', 'last_name',
                  'additional_name', 'birth_date', 'phone', 'email')


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('checkin_date', 'checkout_date')


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ('number',)
