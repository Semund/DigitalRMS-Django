from django.db import models


class Order(model.Models):
    order_create = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey('Customer', on_delete=models.PROTECT)
    time_delivery = models.DateTimeField(auto_now_add=True) # предлагаю order_delivery