from django.shortcuts import render

from .forms import GuestForm, BookingForm, RoomForm
from .models import Booking
from .registration_services import *


# Create your views here.


def _get_checkin_context():
    form_guest = GuestForm()
    form_booking = BookingForm()
    form_room = RoomForm()
    context = {
        'page_title': 'Checkin',
        'form_guest': form_guest,
        'form_booking': form_booking,
        'form_room': form_room
    }

    return context


def _update_checkin_context(context, form_guest, form_booking, form_room):
    context['form_guest'] = form_guest
    context['form_booking'] = form_booking
    context['form_room'] = form_room
    return context


def checkin(request):
    context = _get_checkin_context()
    if request.method == 'POST':
        form_guest = process_guest_data(request.POST)
        form_booking = process_booking_data(request.POST)
        form_room = process_room_data(request.POST)
        context = _update_checkin_context(context, form_guest, form_booking, form_room)
        if check_all_registration_data(form_room, form_booking, form_room):
            guest_id = form_guest.save().id
            room_id = form_room.save().id
            new_booking = Booking(
                checkin_date=form_booking.data['checkin_date'],
                checkout_date=form_booking.data['checkout_date'],
                guest_id=guest_id,
                room_id=room_id
            )
            new_booking.save()
            return redirect('home')

    return render(request, 'registration/checkin.html', context=context)
