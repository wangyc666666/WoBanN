# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-05 09:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0010_auto_20170905_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='videourl',
            field=models.URLField(blank=True, max_length=500, null=True, verbose_name='百度云盘URL'),
        ),
    ]
