# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-13 10:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_comment_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='title',
            field=models.CharField(default=None, max_length=32, verbose_name='title'),
        ),
    ]
