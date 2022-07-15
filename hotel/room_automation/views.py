from django.shortcuts import render

from room_automation.forms import RoomAutomationForm


# Create your views here.
def room_view(request):
    context = {
        'room_select': RoomAutomationForm(),
        'url_api': 'api/v1/rooms/'
    }
    return render(request, 'room_automation/room_automation.html', context=context)
