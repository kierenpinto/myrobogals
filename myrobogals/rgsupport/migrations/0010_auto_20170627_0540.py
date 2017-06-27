# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rgsupport', '0009_auto_20170627_0539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
