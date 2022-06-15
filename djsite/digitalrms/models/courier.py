from django.db import models


class Courier(model.Models):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    photo = models.ImageFields(upload_to = "photos/%Y/%m/%d")   




