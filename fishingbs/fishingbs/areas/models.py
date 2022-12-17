from django.db import models

from fishingbs.mixins.mixins import get_locations


class SearchInFishingAreaModel(models.Model):
    CHOICES = get_locations()

    location = models.CharField(
        max_length=20,
        choices=CHOICES,
    )
