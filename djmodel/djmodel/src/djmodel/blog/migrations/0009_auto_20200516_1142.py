# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2020-05-16 11:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200516_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='publish_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterUniqueTogether(
            name='blogmodel',
            unique_together=set([('title', 'content')]),
        ),
    ]
