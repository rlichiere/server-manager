# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-12-15 16:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('containermanager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='label',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='application',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='environment',
            name='label',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='environment',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]