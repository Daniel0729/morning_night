# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-24 23:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Morning', '0002_auto_20161121_1654'),
    ]

    operations = [
        migrations.RenameField(
            model_name='light_state',
            old_name='name',
            new_name='light',
        ),
        migrations.RenameField(
            model_name='music_state',
            old_name='name',
            new_name='music',
        ),
    ]
