import json

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
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
