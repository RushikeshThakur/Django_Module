# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2020-05-16 09:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='title',
            field=models.CharField(default='New title', max_length=250),
            preserve_default=False,
        ),
    ]