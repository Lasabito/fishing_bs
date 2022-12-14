from django.urls import path

from fishingbs.areas.views import fishing_areas, AreaForecast

urlpatterns = [
    path('map/', fishing_areas, name='fishing areas'),
    path('forecast/<slug:area>/', AreaForecast.as_view(), name='area forecast'),
]


