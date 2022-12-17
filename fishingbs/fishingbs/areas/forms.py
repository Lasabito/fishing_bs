from django import forms

from fishingbs.areas.models import SearchInFishingAreaModel


class SearchInFishingAreaForm(forms.ModelForm):
    class Meta:
        model = SearchInFishingAreaModel
        fields = '__all__'
        widgets = {
            'location': forms.Select(
                attrs={
                    'class': 'location-choices',
                }
            )
        }