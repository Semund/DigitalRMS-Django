from django.db import models
# нужен ли импорт модуля datetime ?


class Booking(model.Models):
    checkin_date = models.DateField()
    checkout_date = models.DateField()
    guest = models.ForeignKey('Guest', on_delete=models.PROTECT)   