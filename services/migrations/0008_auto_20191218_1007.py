# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-12-18 08:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_serviceaddonanswer_ord_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('recived', 'recived'), ('under review', 'under review'), ('rejected', 'rejected'), ('paid', 'paid'), ('processing', 'processing'), ('send to delivary', 'sendToDelivary'), ('delivered', 'delivered'), ('canceled', 'canceled'), ('failed', 'failed')], default='recived', max_length=20),
        ),
    ]
