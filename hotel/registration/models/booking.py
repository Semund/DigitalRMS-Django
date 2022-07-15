from django.db import models

from registration.models.guest import Guest
from registration.models.room import Room


class Booking(models.Model):
    checkin_date = models.DateField(verbose_name='Дата заселения')
    checkout_date = models.DateField(verbose_name='Дата выселения')
    guests = models.ManyToManyField(Guest, related_name='booking_guest')
    room = models.ForeignKey(Room, on_delete=models.PROTECT, verbose_name='Номер')

    class Meta:
        app_label = 'registration'
        verbose_name = 'Проживание'
        verbose_name_plural = 'Проживания'
