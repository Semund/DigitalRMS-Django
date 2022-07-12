import requests

from datetime import datetime, timedelta

from django.conf import settings
from django.core.management import BaseCommand

from main.models import Event


class Command(BaseCommand):
    help = "Get events for NUM days since DATE and add them to DB"
    EVENTS_API_URL = 'https://kudago.com/public-api/v1.4/events/'

    request_parameters = {
        'location': 'spb',
        'page_size': 100,
        'text_format': 'text',
        'fields': 'dates,title,short_title,slug,place,description,images,site_url',
    }

    def add_arguments(self, parser):
        parser.add_argument('-d', '--date', type=str, help='Enter data in YYYY-mm-dd format')
        parser.add_argument('-n', '--num', type=int, help='Enter integer num days')

    def handle(self, *args, **options):
        date_start_scan = datetime.strptime(options['date'], '%Y-%m-%d')
        num_days = options['num']

        timestamp_start = int(datetime.timestamp(date_start_scan))
        timestamp_end = int(datetime.timestamp(date_start_scan + timedelta(days=num_days)))

        self.request_parameters['actual_since'] = timestamp_start
        self.request_parameters['actual_until'] = timestamp_end

        self.get_events_list_from_url_to_db(timestamp_start, timestamp_end)

    def get_events_list_from_url_to_db(self, start: datetime.timestamp, end: datetime.timestamp) -> None:
        try:
            response = requests.get(self.EVENTS_API_URL, params=self.request_parameters)
            if response.status_code == 200:
                for event in response.json()['results']:
                    current_event_dates = []
                    for date in event['dates']:
                        if start <= date['end'] <= end or start <= date['start'] <= end:
                            current_event_dates.append((
                                datetime.fromtimestamp(date['start'], tz=settings.TZONE_INFO),
                                datetime.fromtimestamp(date['end'], tz=settings.TZONE_INFO),
                            ))

                    event_data = {
                        'dates': current_event_dates,
                        'title': event['title'],
                        'description': event['description'],
                        'site_url': event['site_url'],
                        'image_url': event['images'][0]['image']
                    }
                    self.write_event_to_db(event_data)

        except (requests.RequestException,):
            pass  # TODO create logging

    def write_event_to_db(self, event: dict) -> None:
        for date in event['dates']:
            Event.objects.create(
                date_start=date[0],
                date_end=date[1],
                title=event['title'],
                description=event['description'],
                site_url=event['site_url'],
                image_url=event['image_url']
            )
