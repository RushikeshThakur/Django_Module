# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2020-05-16 10:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200516_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='title',
            field=models.CharField(max_length=250, verbose_name='New Title'),
        ),
    ]
