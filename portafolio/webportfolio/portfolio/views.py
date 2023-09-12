from django.shortcuts import render
from django.views.generic import ListView
from .models import Portfolio

# Create your views here.


class PorfolioListViews(ListView):
    model = Portfolio
