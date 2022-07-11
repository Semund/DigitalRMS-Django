from django.db import models


class Weather(models.Model):
    date = models.DateField()
    time = models.TimeField()
    temperature = models.FloatField()
    icon = models.CharField(max_length=3)
    description = models.CharField(max_length=100)

    class Meta:
        ordering = ['date', 'time']

    def __str__(self):
        return f'Погода {self.date} {self.time} - {self.temperature}'
