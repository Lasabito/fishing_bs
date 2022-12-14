from django.urls import path

from fishingbs.news.views import FishInformationView, news_create_view, FishNewsDelete, FishNewUpdate

urlpatterns = [
    path('', FishInformationView.as_view(), name='news'),
    path('create/', news_create_view, name='create news'),
    path('edit/<int:pk>', FishNewUpdate.as_view(), name='edit news'),
    path('delete/<int:pk>', FishNewsDelete.as_view(), name='delete news'),
]
