from django.db import models


class DeliveryList(model.Models):
    is_taken = models.BooleanField()
    courier = models.ForeignKey('Courier', on_delete=models.PROTECT)
    order = models.ForeignKey('Order', on_delete=models.PROTECT)
