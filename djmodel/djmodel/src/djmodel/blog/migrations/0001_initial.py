# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2020-05-16 09:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
