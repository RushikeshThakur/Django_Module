# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2020-05-16 10:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200516_1030'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PostModel',
            new_name='BlogModel',
        ),
    ]