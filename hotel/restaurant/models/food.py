from django.db import models

from restaurant.models.food_category import FoodCategory


class Food(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name='Фото')
    category = models.ForeignKey(FoodCategory, on_delete=models.PROTECT, verbose_name='Категория')

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'
        app_label = 'restaurant'
