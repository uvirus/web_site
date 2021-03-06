# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 05:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subscribers', '0005_auto_20170817_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='created_by_company', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='company',
            name='updated_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='updated_by_company', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='signup',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='created_by_signup', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='signup',
            name='updated_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='updated_by_signup', to=settings.AUTH_USER_MODEL),
        ),
    ]
