# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-10 10:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memo', '0006_auto_20160510_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='memorized_words',
            field=models.ManyToManyField(blank=True, to='memo.Word'),
        ),
    ]
