# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-09-01 17:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subservice',
            name='actions',
            field=models.CharField(blank=True, default='', max_length=400),
        ),
        migrations.AlterField(
            model_name='subservice',
            name='papers',
            field=models.CharField(blank=True, default='', max_length=400),
        ),
    ]