from django.shortcuts import redirect
from django.views.generic import TemplateView

from .forms import GuestForm, BookingForm


class CheckinView(TemplateView):
    template_name = 'registration/checkin.html'
    booking_form_class = BookingForm
    guest_form_class = GuestForm

    def post(self, request, *args, **kwargs):
        post_data = request.POST or None
        form_booking = self.booking_form_class(post_data, prefix='booking')
        form_guest = self.guest_form_class(post_data, prefix='guest')

        context = self.get_context_data(form_booking=form_booking, form_guest=form_guest)

        if form_booking.is_valid() and form_guest.is_valid():
            self.form_save(form_booking, form_guest)
            return redirect('home')

        return self.render_to_response(context)

    def form_save(self, form_booking, form_guest):
        guest = form_guest.save()
        booking = form_booking.save()
        booking.guests.add(guest)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
