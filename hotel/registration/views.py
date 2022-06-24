from django.shortcuts import render

from .forms import GuestForm, BookingForm, RoomForm
from .models import Room


# Create your views here.
def checkin(request):
    room_list = Room.objects.all()
    form_guest = GuestForm()
    form_booking = BookingForm()
    form_room = RoomForm()

    context = {
        'page_title': 'Checkin',
        'room_list': room_list,
        'form_guest': form_guest,
        'form_booking': form_booking,
        'form_room': form_room
    }

    return render(request, 'registration/checkin.html', context=context)
