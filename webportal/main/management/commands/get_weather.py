import requests
from django.core.management import BaseCommand

from main.models import Weather
from webportal.settings_local import WEATHER_API_KEY


class Command(BaseCommand):
    help = "Get weather for 5 days since today and add them to DB"

    WEATHER_API_URL = 'https://api.openweathermap.org/data/2.5/forecast'

    request_parameters = {
        'lat': 59.9167,
        'lon': 30.25,
        'appid': WEATHER_API_KEY,
        'units': 'metric',
        'mode': 'json',
        'lang': 'ru'
    }

    def handle(self, *args, **options):
        try:
            response = requests.get(self.WEATHER_API_URL, params=self.request_parameters)
            if response.status_code == 200:
                Weather.objects.all().delete()
                for w in response.json()['list']:
                    date, time = w['dt_txt'].split()
                    weather = Weather(
                        date=date,
                        time=time,
                        temperature=round(w['main']['temp'], 1),
                        icon=w['weather'][0]['icon'],
                        description=w['weather'][0]['description']
                    )
                    weather.save()

        except (requests.RequestException,):
            pass  # TODO create logging
