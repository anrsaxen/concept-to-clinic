# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-10 18:45
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0007_auto_20171207_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='probability_concerning',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)]),
        ),
    ]
