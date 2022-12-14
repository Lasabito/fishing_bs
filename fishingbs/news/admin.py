from django.contrib import admin

from fishingbs.news.models import GiveInformationModel


@admin.register(GiveInformationModel)
class GiveInformationAdmin(admin.ModelAdmin):
    list_display = ['fish_type', 'location', 'type_of_catching', 'from_user']
