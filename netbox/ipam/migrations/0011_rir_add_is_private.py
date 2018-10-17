# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-06 18:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipam', '0010_ipaddress_help_texts'),
    ]

    operations = [
        migrations.AddField(
            model_name='rir',
            name='is_private',
            field=models.BooleanField(default=False, help_text=b'IP space managed by this RIR is considered private', verbose_name=b'Private'),
        ),
    ]
