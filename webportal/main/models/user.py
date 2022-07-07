from datetime import date

import jwt
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

from webportal import settings


class UserManager(BaseUserManager):

    def create_user(self, room, passport, checkout_date, **extra_fields):
        now = timezone.now()
        user = self.model(
            room=room,
            passport=passport,
            checkout_date=checkout_date,
            last_login=now,
            **extra_fields
        )
        user.set_unusable_password()
        user.save(using=self._db)
        return user

    def create_superuser(self, room, passport, **extra_fields):
        pass
        # user = self._create_user(room, passport, True, True, **extra_fields)
        # return user


class User(AbstractBaseUser, PermissionsMixin):
    passport = models.CharField(max_length=12, unique=True)
    room = models.CharField(max_length=3)
    checkout_date = models.DateField()
    last_login = models.DateTimeField(null=True, blank=True)
    password = None

    USERNAME_FIELD = 'passport'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self):
        return f"/users/{self.pk}/"

    @property
    def token(self):
        return self._generate_jwt_token()

    def get_full_name(self):
        return self.passport

    def get_short_name(self):
        return self.passport

    def _generate_jwt_token(self):
        dt = self.checkout_date - date.today()

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.total_seconds())
        }, settings.SECRET_KEY, algorithm='HS256')

        return token
