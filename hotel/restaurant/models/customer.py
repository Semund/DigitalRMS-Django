from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    room = models.IntegerField(max_length=10, verbose_name='Номер')

    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики'
        app_label = "restaurant"
