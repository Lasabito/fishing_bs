from django import forms

from fishingbs.weather.models import ChooseTownModel


class ChooseTownForm(forms.ModelForm):
    class Meta:
        model = ChooseTownModel
        fields = '__all__'
        widgets = {
            'town': forms.Select(
                attrs={
                    'class': 'town-choices',
                }
            )
        }

