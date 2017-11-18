from django.contrib import admin
from .models import Company


@admin.register(Company)
class SpiritAdmin(admin.ModelAdmin):
    list_display = ("name", "country", "founded")
