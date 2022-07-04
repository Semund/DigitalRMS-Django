from django.db import models


class Guest(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    checkin_date = models.DateField(verbose_name='Дата заселения')
    checkout_date = models.DateField(verbose_name='Дата выселения')
    room = models.IntegerField(verbose_name='Номер')

    class Meta:
        app_label = 'main'
        verbose_name = 'Гость'
        verbose_name_plural = 'Гости'

    def __str__(self):
        return f'Гость {self.name} из номера {self.room}'
