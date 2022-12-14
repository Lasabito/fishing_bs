from django import forms

from fishingbs.news.models import GiveInformationModel


class GiveInformationForm(forms.ModelForm):
    class Meta:
        model = GiveInformationModel
        exclude = ['from_user', 'created_on']
        labels = {
            'fish_type': 'Вид риба',
            'location': 'Локация',
            'intensity': 'Интензивност',
            'last_most_intense': 'Последно най-активен',
            'type_of_catching': 'Начин на роболов',
            'photo': 'Снимка',
            'comment': 'Коментар',
        }
