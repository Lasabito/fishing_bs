from django import forms

from fishingbs.weather_warnings.models import WeatherWarningsModel


class WeatherWarningForm(forms.ModelForm):
    class Meta:
        model = WeatherWarningsModel
        exclude = ['created_on', 'from_user']
        labels = {
            'location': 'Локация',
            'warning_type': 'Вид предупреждение',
            'comment': 'Коментар',
        }
