# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-09-01 18:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20190901_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='paymentType',
            field=models.CharField(choices=[('cash on delivery', 'cash on delivery'), ('visa card', 'visa card')], default='cash on delivery', max_length=20),
        ),
    ]
