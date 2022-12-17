from django.contrib import admin

from fishingbs.weather_warnings.models import WeatherWarningsModel


@admin.register(WeatherWarningsModel)
class WeatherWarningsModelAdmin(admin.ModelAdmin):
    list_display = ['location', 'warning_type', 'from_user']
