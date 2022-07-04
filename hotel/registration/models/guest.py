from django.db import models


class Guest(models.Model):
    passport_number = models.CharField(max_length=16, unique=True, verbose_name='Номер паспорта')
    date_of_issue = models.DateField(verbose_name='Дата выдачи')
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    additional_name = models.CharField(max_length=50, blank=True, verbose_name='Дополнительное имя')
    birth_date = models.DateField(verbose_name='Дата рождения')
    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name='Телефон')
    email = models.CharField(max_length=255, blank=True, null=True, verbose_name='Почта')

    class Meta:
        app_label = 'registration'
        verbose_name = 'Гость'
        verbose_name_plural = 'Гости'
