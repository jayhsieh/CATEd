# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-15 09:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0009_auto_20170615_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallethistory',
            name='value',
            field=models.DecimalField(decimal_places=8, default=0, max_digits=30),
        ),
    ]
