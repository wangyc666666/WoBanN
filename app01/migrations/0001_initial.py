# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-31 06:40
from __future__ import unicode_literals

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='邮件')),
                ('user_valid', models.BooleanField(default=False, verbose_name='是否有效')),
                ('userpic', models.ImageField(default='statics/images/image30.png', upload_to='statics/images/', verbose_name='头像')),
                ('gender', models.CharField(choices=[('M', '男'), ('F', '女')], default='男', max_length=1, verbose_name='性别')),
                ('signature', models.CharField(default='hello world', max_length=100, verbose_name='签名档(100字)')),
                ('focus_count', models.IntegerField(default=0, verbose_name='关注数')),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='用户创建时间')),
                ('focususer', models.ManyToManyField(blank=True, to='app01.Admin')),
            ],
            options={
                'verbose_name_plural': '账户',
                'verbose_name': '账户',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=32, null=True, unique=True, verbose_name='类别')),
                ('administrator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Admin')),
            ],
            options={
                'verbose_name_plural': 'asked导航栏',
                'verbose_name': 'asked导航栏',
            },
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('chat_date', models.DateTimeField(auto_now_add=True, verbose_name='聊天时间')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Admin')),
            ],
            options={
                'verbose_name_plural': '聊天室',
                'verbose_name': '聊天室',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='标题')),
                ('summary', models.CharField(blank=True, max_length=256, null=True, verbose_name='简介')),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='内容')),
                ('video', models.FileField(default='statics/video/20170209130422_Broods.mp3', upload_to='statics/video/', verbose_name='教程(.mp3 .mp4)')),
                ('newpic', models.ImageField(default='statics/upload_imgss/logo.jpg', upload_to='statics/images/', verbose_name='封面图片')),
                ('url', models.URLField(blank=True, default='www.askeds.com/server', null=True, verbose_name='链接地址')),
                ('favor_count', models.IntegerField(default=0, verbose_name='点击数')),
                ('reply_count', models.IntegerField(default=0, verbose_name='评论数')),
                ('focus_count', models.IntegerField(default=0, verbose_name='关注数')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app01.Category')),
                ('focususer', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '发布',
                'verbose_name': '视频教程',
            },
        ),
        migrations.CreateModel(
            name='NewType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display', models.CharField(blank=True, max_length=50, null=True, verbose_name='标签云')),
            ],
            options={
                'verbose_name_plural': '标签云',
                'verbose_name': '标签云',
            },
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='评论时间')),
                ('new', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.News')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Admin')),
            ],
            options={
                'verbose_name_plural': 'asked评论',
                'verbose_name': 'aksed评论',
            },
        ),
        migrations.CreateModel(
            name='serverClient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, verbose_name='访问量类型')),
                ('serverclient', models.IntegerField(default=0, verbose_name='访问量')),
            ],
            options={
                'verbose_name_plural': '访问量',
                'verbose_name': '访问量',
            },
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dispaly', models.CharField(blank=True, max_length=50, null=True, verbose_name='用户类型')),
            ],
            options={
                'verbose_name_plural': '用户类型',
                'verbose_name': '用户类型',
            },
        ),
        migrations.AddField(
            model_name='news',
            name='news_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.NewType'),
        ),
        migrations.AddField(
            model_name='news',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Admin'),
        ),
        migrations.AddField(
            model_name='admin',
            name='user_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app01.UserType'),
        ),
        migrations.AddField(
            model_name='admin',
            name='username',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
