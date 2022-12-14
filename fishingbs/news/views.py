from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from fishingbs.accounts.models import Profile
from fishingbs.mixins.get_filters_count import get_filters_count
from fishingbs.news.forms import GiveInformationForm
from fishingbs.news.models import GiveInformationModel


class FishInformationView(views.ListView):
    model = GiveInformationModel
    template_name = 'news/last_news.html'
    context_object_name = 'news'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = get_filters_count(context, self.model.objects)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        time = self.request.GET.get('time', None)
        fish_type = self.request.GET.get('fish_type', None)
        location = self.request.GET.get('location', None)

        if time:
            if time == 'soonest':
                queryset = queryset.order_by('-created_on')
            else:
                queryset = queryset.order_by('created_on')

        if fish_type and location:
            queryset = queryset.filter(fish_type=fish_type)
            queryset = queryset.filter(location=location)
        elif fish_type:
            queryset = queryset.filter(fish_type=fish_type)
        elif location:
            queryset = queryset.filter(location=location)
        return queryset


def news_create_view(request):
    user = request.user
    if user.id is None:
        return redirect('log in')
    if request.method == 'GET':
        form = GiveInformationForm(label_suffix='')
    else:
        form = GiveInformationForm(request.POST, request.FILES, label_suffix='')
        if form.is_valid():
            news = GiveInformationModel(
                fish_type=form.cleaned_data['fish_type'],
                location=form.cleaned_data['location'],
                intensity=form.cleaned_data['intensity'],
                last_most_intense=form.cleaned_data['last_most_intense'],
                type_of_catching=form.cleaned_data['type_of_catching'],
                photo=form.cleaned_data['photo'],
                comment=form.cleaned_data['comment'],
                from_user=Profile(user=request.user),
            )
            news.save()
            return redirect('news')

    context = {
        'form': form
    }
    return render(request, 'news/create_news.html', context)


class FishNewUpdate(views.UpdateView):
    template_name = 'news/update-news.html'
    model = GiveInformationModel
    form_class = GiveInformationForm
    success_url = reverse_lazy('news')


class FishNewsDelete(views.DeleteView):
    model = GiveInformationModel
    template_name = 'news/delete-news.html'
    success_url = reverse_lazy('news')
