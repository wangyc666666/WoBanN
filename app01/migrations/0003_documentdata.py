# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-02 02:55
from __future__ import unicode_literals

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app01', '0002_auto_20170831_1446'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='标题')),
                ('summary', models.CharField(blank=True, max_length=256, null=True, verbose_name='简介')),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='内容')),
                ('document_data', models.FileField(default='statics/document/20170209130422_Broods.txt', upload_to='statics/document/', verbose_name='文档资料')),
                ('newpic', models.ImageField(default='statics/upload_imgss/logo.jpg', upload_to='statics/images/', verbose_name='封面图片')),
                ('url', models.URLField(blank=True, default='www.askeds.com/server', null=True, verbose_name='链接地址')),
                ('favor_count', models.IntegerField(default=0, verbose_name='点击数')),
                ('reply_count', models.IntegerField(default=0, verbose_name='评论数')),
                ('focus_count', models.IntegerField(default=0, verbose_name='关注数')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app01.Category')),
                ('focususer', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
                ('news_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.NewType')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Admin')),
            ],
            options={
                'verbose_name': '文档资料',
                'verbose_name_plural': '发布',
            },
        ),
    ]
