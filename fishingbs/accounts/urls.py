from django.contrib.auth.views import LogoutView
from django.urls import path

from fishingbs.accounts.views import AppUserCreate, ProfileDetailsView, UserLoginForm, ProfileUpdateView, \
    ProfileDeleteView, not_the_owner

urlpatterns = [
    path('register/', AppUserCreate.as_view(), name='register'),
    path('details/<int:pk>/', ProfileDetailsView.as_view(), name='profile details'),
    path('log-in/', UserLoginForm.as_view(), name='log in'),
    path('log-out/', LogoutView.as_view(), name='log out'),
    path('update/<int:pk>/', ProfileUpdateView.as_view(), name='profile update'),
    path('delete/<int:pk>/', ProfileDeleteView.as_view(), name='profile delete'),
    path('not_having_the_permission/', not_the_owner, name='not the owner page'),
]
