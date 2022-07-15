from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from django.views.generic import TemplateView


class RoomControlView(LoginRequiredMixin, TemplateView):
    login_url = 'authorization'
    template_name = 'room_control/room.html'
    url_room_api = 'http://127.0.0.1:8001/room/api/v1/rooms/'

    def get(self, request, *args, **kwargs):
        guest_name = request.user.name
        guest_room_number = request.user.room

        context = self.get_context_data(guest_name=guest_name,
                                        guest_room_number=guest_room_number,
                                        url_room_api=self.url_room_api,
                                        **kwargs)
        return self.render_to_response(context)
