# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rgsupport', '0008_auto_20170627_0503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 27, 5, 39, 37, 293390, tzinfo=utc)),
        ),
    ]
