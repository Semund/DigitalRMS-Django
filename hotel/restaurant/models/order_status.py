from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=50, verbose_name='Статус')

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'
        app_label = "restaurant"
