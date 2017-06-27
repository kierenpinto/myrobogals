# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rgsupport', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 27, 3, 21, 46, 414607, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
