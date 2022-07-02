import json

from django.http import JsonResponse
from django.shortcuts import render

from room_automation.forms import RoomAutomationForm
from room_automation.models import RoomAutomation


# Create your views here.


def collect_room_automation_data(room_id: int) -> dict:
    room_automation_object = RoomAutomation.objects.get(room_id=room_id)
    room_number = room_automation_object.room.number
    room_light_params = json.loads(room_automation_object.light)
    room_climat_params = json.loads(room_automation_object.climat)
    room_automation_data = {
        'room_number': room_number,
        'room_light': room_light_params,
        'room_climat': room_climat_params
    }
    return room_automation_data


def room_view(request):
    context = {
        'room_select': RoomAutomationForm()
    }

    if request.method == 'POST':
        room_id = int(request.POST['room'])
        room_automation_data = collect_room_automation_data(room_id)
        return JsonResponse(data=room_automation_data)

    return render(request, 'room_automation/room_automation.html', context=context)
