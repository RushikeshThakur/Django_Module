# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2020-05-16 12:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20200516_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]