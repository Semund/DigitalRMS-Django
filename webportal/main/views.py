from django.shortcuts import render


# Create your views here.
def authorization(request):
    context = {
        'page_title': 'Authorization',
        'url_hotel_guest_api': 'http://127.0.0.1:8001/checkin/api/v1/guest'
    }
    return render(request, 'main/authorization.html', context=context)
