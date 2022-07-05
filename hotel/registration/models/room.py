from django.db import models


class Room(models.Model):
    number = models.CharField(verbose_name='Номер', max_length=5)

    def __str__(self):
        return f'Номер {self.number}'

    class Meta:
        app_label = 'registration'
        verbose_name = 'Номер'
        verbose_name_plural = 'Номера'
