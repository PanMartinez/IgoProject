from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=64, verbose_name="name")
    country = models.CharField(max_length=64, verbose_name="country")
    founded = models.IntegerField(null=True, verbose_name="founded")
    logo = models.ImageField(upload_to="static/images", blank=True, null=True)
    description = models.TextField()
    workers = models.ManyToManyField(User, through= "Members")


class Members(models.Model):
    company = models.ForeignKey(Company)
    worker = models.ForeignKey(User)

