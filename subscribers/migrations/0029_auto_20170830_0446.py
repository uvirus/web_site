# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 04:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribers', '0028_auto_20170829_0701'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='company',
            name='updated_date',
        ),
        migrations.RemoveField(
            model_name='subscriber',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='subscriber',
            name='updated_date',
        ),
        migrations.AddField(
            model_name='company',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='updated_on',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='subscriber',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='subscriber',
            name='updated_on',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
