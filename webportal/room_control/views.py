from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class RoomControlView(LoginRequiredMixin, TemplateView):
    login_url = 'authorization'
    template_name = 'room_control/room.html'

    def get(self, request, *args, **kwargs):
        guest_name = request.user.name

        context = self.get_context_data(guest_name=guest_name,
                                        **kwargs)
        return self.render_to_response(context)
