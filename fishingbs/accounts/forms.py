import random

from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model
from django.contrib.auth.forms import UsernameField
from django.forms import ClearableFileInput
from fishingbs import settings
from fishingbs.accounts.models import Profile

UserModel = get_user_model()


def check_for_same_username(username):
    try:
        checker = Profile.objects.filter(username=username).get()
    except:
        checker = False
    return checker


class SignUpForm(auth_forms.UserCreationForm):
    username = forms.CharField(
        max_length=25,
    )

    class Meta:
        model = UserModel
        fields = ('email', 'username')

    def save(self, commit=True):
        user = super().save(commit=commit)
        username = self.cleaned_data['username']

        if check_for_same_username(username):
            profile = Profile(
                user=user,
                username=f'{username}{random.randint(1, 10000)}',
            )
        else:
            profile = Profile(
                user=user,
                username=username,
            )
        if commit:
            profile.save()
        return user


class LogInForm(auth_forms.AuthenticationForm):
    username = UsernameField(
        label_suffix='',
        widget=forms.EmailInput()
    )
    password = forms.CharField(
        strip=False,
        label_suffix='',
        label='Парола',
        validators=settings.AUTH_PASSWORD_VALIDATORS,
        widget=forms.PasswordInput()
    )
    error_messages = {
        "invalid_login": "Комбинацията от Email и парола е грешна. Моля опитайте отново.",
        "inactive": "Този акаунт е неактивен.",
    }


class ProfileUpdateForm(forms.ModelForm, ClearableFileInput):
    class Meta:
        model = Profile
        exclude = ['user']
        labels = {
            'username': 'Потребителско име',
            'first_name': 'Име',
            'last_name': 'Фамилия',
            'age': 'Години',
            'town': 'Град/село',
            'profile_picture': 'Снимка',
        }
