# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-10 09:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memo', '0002_userprofile_daily_words_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vocabulary',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='word',
            name='content',
            field=models.CharField(max_length=100, verbose_name='Content'),
        ),
    ]
