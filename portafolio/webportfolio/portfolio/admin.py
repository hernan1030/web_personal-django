from django.contrib import admin
from .models import Portfolio

# Register your models here.


class PortfoliosAdmin(admin.ModelAdmin):
    readonly_fields = ('create', 'update')


admin.site.register(Portfolio, PortfoliosAdmin)
