# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-20 08:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0015_userexchanges_total_usd'),
    ]

    operations = [
        migrations.AddField(
            model_name='userwallet',
            name='total_usd',
            field=models.DecimalField(decimal_places=8, default=0, max_digits=30),
        ),
    ]
