# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-01 05:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0043_auto_20171129_0620'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentdata',
            name='check_enable',
            field=models.BooleanField(default=False, verbose_name='是否审核'),
        ),
    ]
