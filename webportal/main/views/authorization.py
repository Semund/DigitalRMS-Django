import datetime

import requests
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest
from django.shortcuts import redirect
from django.views.generic import TemplateView

from main.models import User


def check_guest_in_existing_users(data: dict) -> bool:
    existing_users = User.objects.filter(passport=data['passport'], room=data['room'])
    return len(existing_users) > 0


def hotel_guest_data_validation(request: HttpRequest) -> dict | None:
    hotel_url_api = 'http://127.0.0.1:8001/checkin/api/v1/guest'
    passport_data = request.POST['passport']

    guest_data_for_hotel_api = {
        'room_number': request.POST['room'],
        'passport_data': passport_data
    }

    try:
        response = requests.post(url=hotel_url_api, data=guest_data_for_hotel_api)
        if response.status_code == 200:
            guest_data = {
                'name': response.json()['guests'][0]['first_name'],
                'room': response.json()['room'],
                'passport': passport_data,
                'checkin_date': response.json()['checkin_date'],
                'checkout_date': response.json()['checkout_date']
            }
            return guest_data
    except (requests.RequestException,):
        messages.error(request, 'No connection with hotel systems')
        return redirect('authorization')


def register_guest_in_webportal(guest_data: dict) -> None:
    new_guest = User(**guest_data)
    new_guest.save()


def get_user_checkout_datetime(user: User) -> datetime.datetime:
    date = user.checkout_date
    time = datetime.time(hour=12, minute=0, tzinfo=settings.TZONE_INFO)
    return datetime.datetime.combine(date, time)


class AuthorizationView(TemplateView):
    template_name = 'main/authorization.html'

    def authorization_failed(self, request):
        messages.error(request, 'Wrong passport or room data')
        return redirect('authorization')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Authorization'
        return context

    def post(self, request, *args, **kwargs):
        if not check_guest_in_existing_users(request.POST):
            guest_data = hotel_guest_data_validation(request)
            if guest_data:
                register_guest_in_webportal(guest_data)
            else:
                return self.authorization_failed(request)

        user = authenticate(
            request,
            passport=request.POST['passport'],
            room=request.POST['room']
        )
        if user is not None:
            login(request, user)
            guest_datetime = get_user_checkout_datetime(user)
            request.session.set_expiry(guest_datetime)
            return redirect('home')
        else:
            return self.authorization_failed(request)


def logout_view(request):
    logout(request)
    return redirect('authorization')
