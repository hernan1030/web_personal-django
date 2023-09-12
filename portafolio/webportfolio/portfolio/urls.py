from django.urls import path
from .views import PorfolioListViews


urlpatterns = [
    path('', PorfolioListViews.as_view(), name="portfolio"),

]
