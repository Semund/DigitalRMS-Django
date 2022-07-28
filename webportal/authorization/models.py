from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):

    def create_user(self, room, passport, checkout_date, name, checkin_date, **extra_fields):
        now = timezone.now()
        user = self.model(
            room=room,
            passport=passport,
            checkout_date=checkout_date,
            checkin_date=checkin_date,
            name=name,
            last_login=now,
            **extra_fields
        )
        user.set_unusable_password()
        user.save(using=self._db)
        return user

    def create_superuser(self, **extra_fields):
        pass


class User(AbstractBaseUser, PermissionsMixin):
    is_active = models.BooleanField(default=True)
    passport = models.CharField(max_length=12, unique=True)
    room = models.CharField(max_length=3)
    checkout_date = models.DateField()
    checkin_date = models.DateField()
    name = models.CharField(max_length=50)
    last_login = models.DateTimeField(null=True, blank=True)
    password = None

    USERNAME_FIELD = 'passport'
    REQUIRED_FIELDS = ['']

    objects = UserManager()

    def get_absolute_url(self):
        return f"/users/{self.pk}/"

    def get_full_name(self):
        return f'{self.name} - {self.passport}'

    def get_short_name(self):
        return self.name
