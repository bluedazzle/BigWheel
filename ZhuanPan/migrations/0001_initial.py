# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consume',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('c_id', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=15)),
                ('consume_time', models.DateTimeField(max_length=25)),
                ('total', models.FloatField(max_length=10)),
                ('if_play', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone', models.CharField(max_length=15)),
                ('content', models.CharField(max_length=50, null=True, blank=True)),
                ('time', models.DateTimeField(auto_now=True)),
                ('if_exchange', models.BooleanField(default=True)),
                ('fail_message', models.TextField(max_length=100, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
