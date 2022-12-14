from django.contrib.auth import get_user_model, login, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from fishingbs.accounts.forms import SignUpForm, LogInForm, ProfileUpdateForm
from fishingbs.accounts.models import Profile

UserModel = get_user_model()


class AppUserCreate(views.CreateView):
    model = UserModel
    template_name = 'accounts/register.html'
    form_class = SignUpForm

    def get_success_url(self):
        created_obj = self.object
        return reverse_lazy('profile details', kwargs={
            'pk': created_obj.pk,
        })

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class UserLoginForm(LoginView):
    template_name = 'accounts/log-in.html'
    form_class = LogInForm
    authentication_form = LogInForm


class ProfileDetailsView(views.DetailView):
    model = Profile
    template_name = 'accounts/profile.html'
    context_object_name = 'user'


class ProfileUpdateView(views.UpdateView):
    model = Profile
    template_name = 'accounts/profile-update.html'
    form_class = ProfileUpdateForm

    def get_success_url(self):
        created_obj = self.object
        return reverse_lazy('profile details', kwargs={
            'pk': created_obj.pk
        })


class ProfileDeleteView(views.DeleteView):
    model = UserModel
    template_name = 'accounts/delete-user.html'
    success_url = reverse_lazy('home')


