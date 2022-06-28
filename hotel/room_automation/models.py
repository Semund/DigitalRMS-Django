from django.db import models


# Create your models here.
from registration.models import Room


class RoomAutomation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name='Номер')
    light = models.JSONField(verbose_name='Свет')
    climat = models.JSONField(verbose_name='Климат')

    class Meta:
        verbose_name = 'Автоматизация номера'
        verbose_name_plural = 'Автоматизация номеров'
