from django.shortcuts import render
from django.views.generic.list import ListView
from .models import AboutMePerfil

# Create your views here.


class PerfilListViews(ListView):
    template_name = 'about/aboutmeperfil_list.html'
    model = AboutMePerfil
