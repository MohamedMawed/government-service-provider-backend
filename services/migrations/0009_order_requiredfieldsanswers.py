# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-09-03 11:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0008_subserviceparameter_iconname'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='requiredFieldsAnswers',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
