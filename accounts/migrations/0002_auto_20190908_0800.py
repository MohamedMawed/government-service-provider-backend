# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-09-08 06:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='lat',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='lng',
            field=models.FloatField(null=True),
        ),
    ]
