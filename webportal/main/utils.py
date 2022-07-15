from collections import defaultdict
from datetime import date, time, timedelta, datetime

from django.conf import settings

from main.models import Weather, Event


def collect_weather_from_db() -> dict:
    weather_data = Weather.objects.filter(
        date__range=(date.today(), date.today() + timedelta(days=3)),
        time__range=(time(hour=9, tzinfo=settings.TZONE_INFO), time(hour=18, tzinfo=settings.TZONE_INFO))
    )

    weather_for_guest = defaultdict(list)

    for weather in weather_data:
        weather_for_guest[weather.date].append({
            'time': weather.time,
            'temp': weather.temperature,
            'desc': weather.description,
            'icon': weather.icon
        })
    return dict(weather_for_guest)


def collect_events_from_db(guest_checkout_date: datetime.date) -> dict:
    events_data = Event.objects.filter(
        date_end__range=(date.today(), guest_checkout_date),
        date_end__hour__gt=0
    )[:10]

    events_for_guest = {}

    for event in events_data:
        if event.title in events_for_guest:
            events_for_guest[event.title]['dates'].append((event.date_start, event.date_end))
        else:
            events_for_guest[event.title] = {
                'title': event.title,
                'image': event.image_url,
                'url': event.site_url,
                'dates': [(event.date_start, event.date_end)]
            }
    return dict(events_for_guest)
