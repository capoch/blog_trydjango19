# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-14 10:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_location_website'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocationImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_images', to='blog.Post')),
            ],
        ),
        migrations.AlterModelOptions(
            name='location',
            options={'ordering': ['-rating', 'name']},
        ),
        migrations.AddField(
            model_name='location',
            name='cuisine',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='locationimage',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location_images', to='blog.Location'),
        ),
    ]
