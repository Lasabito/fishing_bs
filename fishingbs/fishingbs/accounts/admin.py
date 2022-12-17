from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model
from django.utils.translation import gettext_lazy as _

from fishingbs.accounts.forms import SignUpForm
from fishingbs.accounts.models import Profile

UserModel = get_user_model()


@admin.register(UserModel)
class AppUserAdmin(auth_admin.UserAdmin):
    list_display = ['email', 'last_login', 'is_superuser', 'is_staff']
    list_filter = []
    ordering = ['email']
    add_form = SignUpForm
    fieldsets = []
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "username", "password1", "password2"),
            },
        ),
    )
    fields = []


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['username']
