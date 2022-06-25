from django.forms import ModelForm
from django.http import QueryDict
from django.shortcuts import redirect

from registration.forms import GuestForm, BookingForm, RoomForm


def process_guest_data(data: QueryDict) -> ModelForm:
    form_guest = GuestForm(data)
    return form_guest


def process_booking_data(data: QueryDict) -> ModelForm:
    form_booking = BookingForm(data)
    return form_booking


def process_room_data(data: QueryDict) -> ModelForm:
    form_room = RoomForm(data)
    return form_room


def check_all_registration_data(guest: ModelForm, booking: ModelForm, room: ModelForm) -> bool:
    return all((guest.is_valid(), booking.is_valid(), room.is_valid()))
