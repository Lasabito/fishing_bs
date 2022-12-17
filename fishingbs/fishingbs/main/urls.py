from django.urls import path

from fishingbs.main.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
]