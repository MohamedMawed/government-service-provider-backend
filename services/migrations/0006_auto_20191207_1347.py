# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-12-07 11:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import services.models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_serviceaddon'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceAddonAnswer',
            fields=[
                ('srv_addon_answer_id', models.AutoField(primary_key=True, serialize=False)),
                ('file', models.ImageField(upload_to=services.models.upload_Addon_Image)),
            ],
        ),
        migrations.RenameField(
            model_name='serviceparameteranswer',
            old_name='parm_name',
            new_name='parm_answer',
        ),
        migrations.RemoveField(
            model_name='serviceaddon',
            name='file',
        ),
        migrations.AddField(
            model_name='serviceaddonanswer',
            name='addon_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='services.ServiceAddon'),
        ),
    ]
