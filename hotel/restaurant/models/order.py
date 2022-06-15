from django.db import models

from restaurant.models.customer import Customer
from restaurant.models.order_status import Status


class Order(models.Model):
    order_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, verbose_name='Заказчик')
    order_delivery = models.DateTimeField(auto_now=True, verbose_name='Дата доставки')
    order_status = models.ForeignKey(Status, on_delete=models.PROTECT, verbose_name='Статус')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        app_label = "restaurant"
