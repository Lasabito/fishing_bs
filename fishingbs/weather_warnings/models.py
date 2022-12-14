from django.db import models

from fishingbs.accounts.models import Profile
from fishingbs.mixins.mixins import get_max_length_of_a_sequence
from fishingbs.mixins.warnings import get_warnings


class WeatherWarningsModel(models.Model):
    WARNING_TYPE_CHOICES = get_warnings()
    WARNING_TYPE_MAX_LENGTH = get_max_length_of_a_sequence(WARNING_TYPE_CHOICES)

    location = models.CharField(
        max_length=20,
        default='Бургаски залив',
        null=False,
        blank=False,
    )
    warning_type = models.CharField(
        max_length=WARNING_TYPE_MAX_LENGTH,
        choices=WARNING_TYPE_CHOICES,
        null=False,
        blank=False,
    )
    comment = models.TextField(
        max_length=300,
        null=True,
        blank=True,
    )
    created_on = models.DateTimeField(
        auto_now=True,
        null=False,
        blank=False,
    )
    from_user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        default=1,
        blank=False,
        null=False,
    )
