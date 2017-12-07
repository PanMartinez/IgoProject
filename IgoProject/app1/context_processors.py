import datetime
from .models import Company, Comment
from django.contrib.auth.models import User


def my_cp(request):
    ctx = {
        "date": datetime.date.today(),
        'version': "v. 1.1"
    }
    return ctx


def companies(request):
    ctx = {
        "companies": Company.objects.all()
    }
    return ctx


def users(request):
    ctx = {
        "users": User.objects.all()
    }
    return ctx

def comments(request):
    ctx = {
        "comments": Comment.objects.all()
    }
    return ctx