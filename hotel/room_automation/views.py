from django.shortcuts import render

# Create your views here.
from registration.models import Room
from room_automation.forms import RoomAutomationForm


def room_view(request):
    context = {
        'room_select': RoomAutomationForm()
    }

    if request.method == 'POST':
        form_select = RoomAutomationForm(request.POST)
        context['room_select'] = form_select
        context['test_select'] = Room.objects.get(pk=int(request.POST['room']))
        return render(request, 'room_automation/room_automation.html', context=context)

    return render(request, 'room_automation/room_automation.html', context=context)
