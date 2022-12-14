from django.shortcuts import render
from fishingbs.weather.forms import ChooseTownForm
from fishingbs.weather.utils import get_weather_information


def city_forecast_view(request):
    form = ChooseTownForm()
    weather = None
    if 'town' in request.GET:
        town = request.GET.get('town')
        form = ChooseTownForm(request.GET)
        weather = get_weather_information(town)

    is_weather = True if weather else False

    context = {
        'form': form,
        'is_weather': is_weather,
        'temperature': weather['temperature'],
        'feels_like': weather['feels_like'],
        'icon': weather['icon'],
        'sunrise': weather['sunrise'],
        'sunset': weather['sunset'],
        'visibility': weather['visibility'],
        'wind_speed': weather['wind_speed'],
        'wind_direction': weather['wind_direction'],
        'humidity': weather['humidity'],
        'condition': weather['condition'],
        'location': weather['town'],
    } if is_weather else {
        'form': form,
        'is_weather': is_weather,
    }
    return render(request, 'weather/city-forecast.html', context)
