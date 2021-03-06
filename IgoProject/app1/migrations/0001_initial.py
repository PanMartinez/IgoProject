# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 10:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='name')),
                ('country', models.CharField(max_length=64, verbose_name='country')),
                ('founded', models.IntegerField(null=True, verbose_name='founded')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='static/images')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Company')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='workers',
            field=models.ManyToManyField(through='app1.Members', to=settings.AUTH_USER_MODEL),
        ),
    ]
