# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-11 07:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memo', '0007_auto_20160511_0804'),
    ]

    operations = [
        migrations.AddField(
            model_name='learningword',
            name='status',
            field=models.SmallIntegerField(default=3, verbose_name='Word Status'),
        ),
    ]
