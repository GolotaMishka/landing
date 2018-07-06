# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-07-06 21:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='name', max_length=128, null=True)),
                ('phone_number', models.CharField(default='number', max_length=12, null=True)),
                ('level', models.CharField(default='level', max_length=128, null=True)),
                ('place', models.CharField(default='place', max_length=128, null=True)),
            ],
            options={
                'verbose_name': 'MySubscriber',
                'verbose_name_plural': 'A lot of Subscribers',
            },
        ),
    ]
