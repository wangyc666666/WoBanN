# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-12 03:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0018_auto_20171112_0255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin',
            name='buy_car',
        ),
    ]
