import datetime
from .models import Company
from django.contrib.auth.models import User


def my_cp(request):
    ctx = {
        "date": datetime.date.today(),
        'version' : "v. 1.0"
    }
    return ctx


def companies(request):
    ctx = {
        "companies" : Company.objects.all()
    }
    return ctx


def users(request):
    ctx = {
        "users" : User.objects.all()
    }
    return ctx

