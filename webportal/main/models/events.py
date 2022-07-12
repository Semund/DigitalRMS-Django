from django.db import models


class Event(models.Model):
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.URLField()
    site_url = models.URLField()

    class Meta:
        ordering = ['date_start', 'date_end']

    def __str__(self):
        return f'Мероприятие {self.title} from {self.date_start} to {self.date_end}'
