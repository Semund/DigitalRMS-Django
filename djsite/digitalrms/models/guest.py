from django.db import models


class Guest(model.Models):
    passport_number = models.CharField(max_length=15)
    date_of_issue = models.DateField() 
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    additional_name = models.CharField(max_length=50, blank = True)
    birth_date = models.DateField()
    phone = models.CharField(max_length=20, blank = True)
    email = models.CharField(max_length=255, blank = True)
