from django.db import models


# Create your models here.
from registration.models import Room


class RoomAutomation(models.Model):
    number = models.IntegerField(verbose_name='Номер', null=False, unique=True)
    light = models.JSONField(verbose_name='Свет')
    climat = models.JSONField(verbose_name='Климат')

    class Meta:
        verbose_name = 'Автоматизация номера'
        verbose_name_plural = 'Автоматизация номеров'
        ordering = ['number']

    def __str__(self):
        return f'Номер {self.number}'
