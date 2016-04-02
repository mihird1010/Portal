# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20160320_1116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scheme',
            name='id',
        ),
        migrations.AlterField(
            model_name='scheme',
            name='number',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
    ]
