from enum import Enum

from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth import models as auth_models


class UserManager(auth_models.BaseUserManager):
    def create_user(
            self,
            first_name: str,
            last_name: str,
            email: str,
            phone_number: str,
            city: str,
            password: str = None,
            is_staff=False,
            is_superuser=False,
    ) -> "User":
        if not email:
            raise ValueError("User must have an email")
        if not first_name:
            raise ValueError("User must have a first name")
        if not last_name:
            raise ValueError("User must have a last name")
        if not phone_number:
            raise ValueError("User must have a phone number")
        if not city:
            raise ValueError("User must have a city")
        user = self.model(email=self.normalize_email(email))
        user.first_name = first_name
        user.last_name = last_name
        user.phone_number = phone_number
        user.city = city
        user.set_password(password)
        user.is_active = True
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save()

        return user

    def create_superuser(
            self, first_name: str, last_name: str, email: str, phone_number: str, city: str, password: str
    ) -> "User":
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            password=password,
            city=city,
            is_staff=True,
            is_superuser=True,
        )
        user.save()

        return user


class User(auth_models.AbstractUser):
    first_name = models.CharField(verbose_name="First Name", max_length=255)
    last_name = models.CharField(verbose_name="Last Name", max_length=255)
    email = models.EmailField(verbose_name="Email", max_length=255, unique=True)
    phone_number = models.CharField(verbose_name="Phone number",
                                    validators=[RegexValidator('^\d{9}$', message='incorrect format of phone number')],
                                    max_length=9, unique=True)
    city = models.CharField(verbose_name="City", max_length=255)
    password = models.CharField(max_length=255)
    username = None

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "phone_number", "city"]