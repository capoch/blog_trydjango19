# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-14 03:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='rating',
            field=models.DecimalField(decimal_places=1, max_digits=2),
        ),
    ]