import json

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from registration.models import Room
from room_automation.forms import RoomAutomationForm
from room_automation.models import RoomAutomation


def room_view(request):
    context = {
        'room_select': RoomAutomationForm()
    }

    if request.method == 'POST':
        room_id = int(request.POST['room'])
        room_number = Room.objects.get(pk=room_id).number
        room_automation = RoomAutomation.objects.get(pk=room_id)
        room_light = json.loads(room_automation.light)
        room_climat = json.loads(room_automation.climat)
        room_all_params = {
            'room_number': room_number,
            'room_light': room_light,
            'room_climat': room_climat
        }

        return JsonResponse(data=room_all_params)

    return render(request, 'room_automation/room_automation.html', context=context)


class RoomAutomationView(TemplateView):
    template_name = 'room_automation/room_test.html'
    room_select_class = RoomAutomationForm

    def post(self, request, *args, **kwargs):
        post_data = request.POST or None
        room_select_form = self.room_select_class(post_data)
        context = self.get_context_data(room_select_form=room_select_form)
        if room_select_form.is_valid():
            self.collect_room_json_data(room_id=post_data['room'])

        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def collect_room_json_data(self, room_id):
        try:
            room_parameters = RoomAutomation.objects.get(pk=int(room_id))
        except (ValueError,):
            room_parameters = None  # TODO error handling

        return JsonResponse(data={
            'room_number': room_parameters.room.number,
            'room_light_parameters': json.loads(room_parameters.light),
            'room_climat_parameters': json.loads(room_parameters.climat)
        })

