# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-20 18:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_auto_20180220_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
