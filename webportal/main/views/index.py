import datetime
from collections import defaultdict
from datetime import date, timedelta, time

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

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
    )[:30]

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


class IndexView(LoginRequiredMixin, TemplateView):
    login_url = 'authorization'
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Main'
        return context

    def get(self, request, *args, **kwargs):
        guest_name = request.user.name

        weather_for_guest = collect_weather_from_db()
        events_for_guest = collect_events_from_db(request.user.checkout_date)
        print(events_for_guest)
        context = self.get_context_data(weather=weather_for_guest,
                                        events=events_for_guest,
                                        guest_name=guest_name,
                                        **kwargs)
        return self.render_to_response(context)
