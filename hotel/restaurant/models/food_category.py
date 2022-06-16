from django.db import models


class FoodCategory(models.Model):
    name = models.CharField(max_length=50, verbose_name='Категория')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        app_label = "restaurant"
