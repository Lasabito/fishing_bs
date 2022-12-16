import datetime

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth import models as auth_models
from django.core.validators import MinLengthValidator
from django.db import models

from fishingbs.accounts.managers import AppUserManager
from fishingbs.accounts.validators import age_validator, image_max_size_validator, chars_only_validator


class AppUser(AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        unique=True,
        blank=False,
        null=False,
    )
    first_logged = models.DateTimeField(
        auto_now_add=True,
        blank=False,
        null=False,
    )
    is_staff = models.BooleanField(
        default=False,
        blank=False,
        null=False,
    )

    USERNAME_FIELD = 'email'

    objects = AppUserManager()

    def __str__(self):
        return self.email


class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 25
    LAST_NAME_MAX_LENGTH = 25

    profile_picture = models.ImageField(
        upload_to='profile_pictures/',
        validators=(
            image_max_size_validator,
        ),
        blank=True,
        null=True,
    )
    username = models.CharField(
        max_length=25,
        unique=True,
    )
    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        validators=(
            MinLengthValidator(2),
        ),
        max_length=LAST_NAME_MAX_LENGTH,
        blank=True,
        null=True,
    )
    age = models.PositiveIntegerField(
        validators=(
            age_validator,
        ),
        blank=True,
        null=True,
    )
    town = models.CharField(
        validators=(
            chars_only_validator,
        ),
        max_length=20,
        blank=True,
        null=True,
    )
    user = models.OneToOneField(
        AppUser,
        primary_key=True,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.username

    @property
    def get_full_name(self):
        if not self.first_name and not self.last_name:
            return None
        elif self.first_name and not self.last_name:
            return self.first_name
        elif not self.first_name and self.last_name:
            return self.last_name
        else:
            return f'{self.first_name} {self.last_name}'


