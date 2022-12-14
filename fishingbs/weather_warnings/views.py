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
    }
    return render(request, 'weather_warnings/add_weather_warning.html', context)


class UpdateWarning(views.UpdateView):
    model = WeatherWarningsModel
    template_name = 'weather_warnings/update-warning.html'
    form_class = WeatherWarningForm
    success_url = reverse_lazy('warnings')


class DeleteWarning(views.DeleteView):
    model = WeatherWarningsModel
    template_name = 'weather_warnings/delete-warning.html'
    success_url = reverse_lazy('warnings')
