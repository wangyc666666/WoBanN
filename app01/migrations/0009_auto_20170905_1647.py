# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-05 08:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0008_auto_20170905_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='statics/video/', verbose_name='教程(.mp3 .mp4)'),
        ),
        migrations.AlterField(
            model_name='news',
            name='videourl',
            field=models.URLField(blank=True, null=True, verbose_name='百度云盘URL'),
        ),
        migrations.AlterField(
            model_name='news',
            name='weixinnum',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='微信号(可选)'),
        ),
    ]
