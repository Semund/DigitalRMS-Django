from django.db import models


class Food(model.Models):
    menu_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)    
    photo = models.ImageFields(upload_to = "photos/%Y/%m/%d")
    stock =  models.IntegerFloatField