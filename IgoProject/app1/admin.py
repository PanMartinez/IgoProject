from django.contrib import admin
from .models import Company, Comment


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "country", "founded")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("content",)