from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import timezone
from django.contrib.auth.models import User



class Company(models.Model):
    name = models.CharField(max_length=64, verbose_name="name")
    country = models.CharField(max_length=64, verbose_name="country")
    founded = models.IntegerField(null=True,
                                  verbose_name="founded",
                                  validators=[MaxValueValidator(2018), MinValueValidator(1800)])
    logo = models.ImageField(upload_to="static/images", blank=True, null=True)
    description = models.TextField()

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def __str__(self):
        return "{}".format(self.name)


class Comment(models.Model):
    title = models.CharField(max_length=32, verbose_name="title", default=None)
    content = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    user = models.ForeignKey(User)
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.content)


