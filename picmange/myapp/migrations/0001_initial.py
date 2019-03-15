# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-02-28 05:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('photo', models.ImageField(upload_to='')),
                ('createtime', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]