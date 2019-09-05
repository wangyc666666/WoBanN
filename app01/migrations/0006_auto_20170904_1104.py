# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-04 03:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_auto_20170904_1042'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='course_price',
            field=models.IntegerField(blank=True, default='0', verbose_name='课程价格(默认免费)'),
        ),
        migrations.AddField(
            model_name='news',
            name='weixinnum',
            field=models.IntegerField(blank=True, null=True, verbose_name='微信号(可选)'),
        ),
    ]