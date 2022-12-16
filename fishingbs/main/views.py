from django.shortcuts import render
from django.views import generic as views


class IndexView(views.TemplateView):
    template_name = 'index.html'
    extra_context = {
        'title': 'Начало'
    }



