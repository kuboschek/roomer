# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-05-02 05:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allocation', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CollegePhase',
        ),
        migrations.AddField(
            model_name='roomphase',
            name='is_quiet_phase',
            field=models.BooleanField(default=False),
        ),
    ]
