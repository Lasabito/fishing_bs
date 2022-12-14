from django.urls import path

from fishingbs.weather_warnings.views import WarningsView, create_warning, UpdateWarning, DeleteWarning

urlpatterns = [
    path('', WarningsView.as_view(), name='warnings'),
    path('create/', create_warning, name='create warning'),
    path('update/<int:pk>', UpdateWarning.as_view(), name='update warning'),
    path('delete/<int:pk>', DeleteWarning.as_view(), name='delete warning'),
]
