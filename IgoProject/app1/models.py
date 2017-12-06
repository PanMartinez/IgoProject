from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator


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
        ordering = ["name", "country", "founded"]
