from django.db import models


class Courier(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name='Фото')

    class Meta:
        verbose_name = 'Курьер'
        verbose_name_plural = 'Курьеры'
        app_label = "restaurant"
