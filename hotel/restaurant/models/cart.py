from django.db import models

from restaurant.models.order import Order
from restaurant.models.food import Food


class Cart(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, verbose_name='Заказ')
    food = models.ForeignKey(Food, on_delete=models.PROTECT, verbose_name='Блюдо')
    quantity = models.IntegerField(verbose_name='Количество')

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
        app_label = "restaurant"
