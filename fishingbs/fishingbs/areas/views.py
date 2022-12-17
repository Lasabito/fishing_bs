from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import generic as views
from fishingbs.areas.forms import SearchInFishingAreaForm


def fishing_areas(request):
    if request.method == 'GET':
        form = SearchInFishingAreaForm()
    else:
        form = SearchInFishingAreaForm(request.POST)
        if form.is_valid():
            area = form.cleaned_data['location']
            return redirect('area forecast', area=area)
    context = {
        'form': form,
        'title': 'Риболовни райони',
    }
    return render(request, 'locations/fishing-areas.html', context)


class AreaForecast(views.TemplateView, LoginRequiredMixin):
    template_name = 'weather/area-forecast.html'
    extra_context = {
        'title': 'Прогноза за район',
    }
