# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-16 22:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Xinlang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_time', models.DateTimeField()),
                ('time_id', models.CharField(max_length=255)),
                ('news', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'xinlang',
            },
        ),
    ]
