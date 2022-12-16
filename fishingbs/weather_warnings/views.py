from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from fishingbs.accounts.models import Profile
from fishingbs.weather_warnings.forms import WeatherWarningForm
from fishingbs.weather_warnings.models import WeatherWarningsModel


class WarningsView(views.ListView):
    model = WeatherWarningsModel
    template_name = 'weather_warnings/all_warnings.html'
    context_object_name = 'warnings'
    paginate_by = 5
    extra_context = {
        'title': 'Предупреждения',
    }

    def get_queryset(self):
        queryset = super().get_queryset()

        queryset = queryset.order_by('-created_on')

        return queryset


@login_required
def create_warning(request):
    user = request.user
    if user.id is None:
        return redirect('log in')
    if request.method == 'GET':
        form = WeatherWarningForm(label_suffix='')
    else:
        form = WeatherWarningForm(request.POST, label_suffix='')
        if form.is_valid():
            warning = WeatherWarningsModel(
                location=form.cleaned_data['location'],
                warning_type=form.cleaned_data['warning_type'],
                comment=form.cleaned_data['comment'],
                from_user=Profile(user=request.user),
            )
            warning.save()
            return redirect('warnings')

    context = {
        'form': form,
        'title': 'Добавяне на новина',
    }
    return render(request, 'weather_warnings/add_weather_warning.html', context)


class UpdateWarning(LoginRequiredMixin, views.UpdateView):
    model = WeatherWarningsModel
    template_name = 'weather_warnings/update-warning.html'
    form_class = WeatherWarningForm
    success_url = reverse_lazy('warnings')
    extra_context = {
        'title': 'Редактиране на новина',
    }

    def get(self, request, *args, **kwargs):
        result = super().get(request, *args, **kwargs)
        current_user = Profile.objects.filter(pk=self.object.from_user_id).get()
        if request.user == current_user.user or request.user.is_staff:
            return result
        else:
            return redirect('not the owner page')


class DeleteWarning(LoginRequiredMixin, views.DeleteView):
    model = WeatherWarningsModel
    template_name = 'weather_warnings/delete-warning.html'
    success_url = reverse_lazy('warnings')
    extra_context = {
        'title': 'Изтриване на предупреждение',
    }

    def get(self, request, *args, **kwargs):
        result = super().get(request, *args, **kwargs)
        current_user = Profile.objects.filter(pk=self.object.from_user_id).get()
        if request.user == current_user.user or request.user.is_staff:
            return result
        else:
            return redirect('not the owner page')

