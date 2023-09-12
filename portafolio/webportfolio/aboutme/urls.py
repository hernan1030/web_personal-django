from django.urls import path
from .views import PerfilListViews


urlpatterns = [
    path('', PerfilListViews.as_view(), name="about"),

]
