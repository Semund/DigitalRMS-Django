from django.db import models


# Create your models here.
class RoomAutomation(models.Model):
    room_number = models.IntegerField(verbose_name='Номер')
    light = models.JSONField(verbose_name='Свет')
    climat = models.JSONField(verbose_name='Климат')

    class Meta:
        verbose_name = 'Автоматизация номера'
        verbose_name_plural = 'Автоматизация номеров'
