# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-21 11:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20180221_1059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='bio',
        ),
        migrations.AddField(
            model_name='patient',
            name='bio',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]