# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='scheme',
            name='number',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='scheme',
            name='age',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='scheme',
            name='caste',
            field=models.PositiveSmallIntegerField(default=1, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='scheme',
            name='categories',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='scheme',
            name='content',
            field=models.CharField(max_length=10000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='scheme',
            name='duration',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='scheme',
            name='gender',
            field=models.PositiveSmallIntegerField(default=1, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='scheme',
            name='income_per_annum',
            field=models.PositiveSmallIntegerField(default=1, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='scheme',
            name='name',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='scheme',
            name='occupation',
            field=models.PositiveSmallIntegerField(default=1, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='scheme',
            name='physically_handicapped',
            field=models.PositiveSmallIntegerField(default=1, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='scheme',
            name='qualification',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='scheme',
            name='state',
            field=models.PositiveSmallIntegerField(default=1, null=True, blank=True),
        ),
    ]
