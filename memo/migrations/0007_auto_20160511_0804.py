# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-11 00:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('memo', '0006_auto_20160511_0723'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Memo',
            new_name='Note',
        ),
    ]