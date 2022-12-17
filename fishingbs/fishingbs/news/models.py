import datetime

import requests
from django.contrib.auth import get_user_model
from django.db import models

from fishingbs.accounts.models import Profile
from fishingbs.accounts.validators import image_max_size_validator
from fishingbs.mixins import mixins as get


UserModel = get_user_model()


class GiveInformationModel(models.Model):
    FISH_TYPES = get.get_fish_types()
    LOCATIONS = get.get_locations_for_news()
    INTENSITIES = get.get_intensities()
    CATCHING_TYPES = get.get_catching_types()
    MAX_LENGTH_FISH_TYPES = get.get_max_length_of_a_sequence(FISH_TYPES)
    MAX_LENGTH_LOCATIONS = get.get_max_length_of_a_sequence(LOCATIONS)
    MAX_LENGTH_INTENSITIES = get.get_max_length_of_a_sequence(INTENSITIES)
    MAX_LENGTH_CATCHING_TYPES = get.get_max_length_of_a_sequence(CATCHING_TYPES)

    fish_type = models.CharField(
        max_length=MAX_LENGTH_FISH_TYPES,
        choices=FISH_TYPES,
        blank=False,
        null=False,
    )
    location = models.CharField(
        max_length=MAX_LENGTH_LOCATIONS,
        choices=LOCATIONS,
        blank=False,
        null=False,
    )
    intensity = models.CharField(
        max_length=MAX_LENGTH_INTENSITIES,
        choices=INTENSITIES,
        blank=False,
        null=False,
    )
    last_most_intense = models.TimeField(
        default=datetime.datetime.now,
        blank=False,
        null=False,
    )
    type_of_catching = models.CharField(
        max_length=MAX_LENGTH_CATCHING_TYPES,
        choices=CATCHING_TYPES,
        blank=False,
        null=False,
    )
    photo = models.ImageField(
        upload_to='catches/',
        validators=[
            image_max_size_validator,
        ],
        blank=True,
        null=True,
    )
    comment = models.TextField(
        max_length=1500,
        blank=True,
        null=True,
    )
    created_on = models.DateTimeField(
        auto_now_add=True,
    )
    from_user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        default=1,
    )

