# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-14 10:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170914_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='delivery_avaiable',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='location',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
