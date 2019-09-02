# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-09-01 18:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20190901_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('recived', 'recived'), ('paid', 'paid'), ('processing', 'processing'), ('sendToDelivary', 'sendToDelivary'), ('canceled', 'canceled'), ('failed', 'failed')], default='recived', max_length=20),
        ),
    ]
