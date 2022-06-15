from django.db import models

from restaurant.models.courier import Courier
from restaurant.models.order import Order


class DeliveryList(models.Model):
    is_taken = models.BooleanField(verbose_name='У курьера')
    courier = models.ForeignKey(Courier, on_delete=models.PROTECT, verbose_name='Курьер')
    order = models.ForeignKey(Order, on_delete=models.PROTECT, verbose_name='Заказ')

    class Meta:
        verbose_name = 'Лист заказов'
        app_label = "restaurant"
