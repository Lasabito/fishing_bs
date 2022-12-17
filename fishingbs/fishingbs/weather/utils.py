from datetime import datetime
import requests
from translate import Translator


def degrees_to_cardinal(d):
    dirs = [
        'Север',
        'Север',
        'Североизток',
        'Североизток',
        'Изток',
        'Изток',
        'Югоизток',
        'Югоизток',
        'Юг',
        'Юг',
        'Югозапад',
        'Югозапад',
        'Запад',
        'Запад',
        'Северозапад',
        'Северозапад'
    ]
    ix = round(d / (360. / len(dirs)))
    return dirs[ix % len(dirs)]


def to_celsius(temp_f):
    return round(((temp_f - 32) * 0.5556), 2)


def from_unix_to_datetime(unix_code):
    return datetime.fromtimestamp(unix_code)


def translate(string):
    translator = Translator(to_lang='Bulgarian')
    translated = translator.translate(string)
    string = string.lower()
    if string == 'atiya':
        translated = 'Атия'
    elif string == 'ravda':
        translated = 'Равда'
    elif string == 'sozopol':
        translated = 'Созопол'
    return translated


def setup_timedata(data):
    data = str(from_unix_to_datetime(data)).split(', ')
    data = data[-1:-4:-1]
    data = data[0].split(' ')[1]
    data = data.split(':')[:2:]
    data = ':'.join(data)
    return data


def setup_icon_url(icon_name):
    url = f'images/weather/icons/{icon_name}@2x.png'
    return url


def setup_needed_weather(weather):
    weather_dict = {
        'temperature': int(round(to_celsius(weather['main']['temp']), 0)),
        'feels_like': int(round(to_celsius(weather['main']['feels_like']), 0)),
        'icon': setup_icon_url(weather['weather'][0]['icon']),
        'sunrise': setup_timedata(weather['sys']['sunrise']),
        'sunset': setup_timedata(weather['sys']['sunset']),
        'visibility': weather['visibility'],
        'wind_speed': int(round(weather['wind']['speed'], 0)),
        'wind_direction': degrees_to_cardinal(weather['wind']['deg']),
        'humidity': f"{weather['main']['humidity']}%",
        'condition': translate(weather['weather'][0]['main']),
        'town': translate(weather['name']),
    }
    return weather_dict


def get_weather_information(town):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={town}&units=imperial&appid=119a0b4be46c1810b37d0df198a246ae'
    city_weather = requests.get(url).json()
    return setup_needed_weather(city_weather)
