from django.shortcuts import render

# vistas basadas en clases
from django.views.generic import TemplateView

# Create your views here.


class HomeViews(TemplateView):
    template_name = 'core/home.html'
