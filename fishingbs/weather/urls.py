from django.urls import path

from fishingbs.weather.views import city_forecast_view

urlpatterns = [
    path('city-forecast/', city_forecast_view, name='city forecast')
]
