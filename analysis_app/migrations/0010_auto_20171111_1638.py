# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-12 00:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis_app', '0009_trips'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trips',
            name='trip_id',
            field=models.IntegerField(),
        ),
    ]
