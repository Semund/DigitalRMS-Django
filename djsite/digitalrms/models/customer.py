from django.db import models


class Customer(model.Models):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    room = models.IntegerField(max_length=10)