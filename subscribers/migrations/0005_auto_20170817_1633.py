# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-17 16:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscribers', '0004_auto_20170816_1224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='b',
            name='a',
        ),
        migrations.DeleteModel(
            name='A',
        ),
        migrations.DeleteModel(
            name='B',
        ),
    ]