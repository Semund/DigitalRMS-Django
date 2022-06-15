from django.db import models


class Room(model.Models):
    room_number = models.IntegerField(max_length=10)
    
