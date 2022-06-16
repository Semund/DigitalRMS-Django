from django.db import models

from restaurant.models.customer import Customer
from restaurant.models.order_status import OrderStatus


class Order(models.Model):
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, verbose_name='Заказчик')
    time_delivery = models.DateTimeField(auto_now=True, verbose_name='Дата доставки')
    status = models.ForeignKey(OrderStatus, on_delete=models.PROTECT, verbose_name='Статус')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        app_label = "restaurant"
