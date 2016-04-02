# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scheme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('content', models.CharField(max_length=10000)),
                ('state', models.PositiveSmallIntegerField(default=1)),
                ('duration', models.IntegerField()),
                ('qualification', models.PositiveSmallIntegerField()),
                ('income_per_annum', models.PositiveSmallIntegerField(default=1)),
                ('caste', models.PositiveSmallIntegerField(default=1)),
                ('physically_handicapped', models.PositiveSmallIntegerField(default=1)),
                ('gender', models.PositiveSmallIntegerField(default=1)),
                ('age', models.CharField(max_length=50)),
                ('occupation', models.PositiveSmallIntegerField(default=1)),
                ('categories', models.CharField(max_length=100)),
            ],
        ),
    ]
