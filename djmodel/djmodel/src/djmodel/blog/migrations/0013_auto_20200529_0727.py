# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2020-05-29 07:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20200529_0721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='email',
            field=models.EmailField(max_length=250),
        ),
    ]
