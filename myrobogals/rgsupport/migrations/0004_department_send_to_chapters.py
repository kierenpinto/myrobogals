# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rgsupport', '0003_auto_20170627_0330'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='send_to_chapters',
            field=models.BooleanField(default=False),
        ),
    ]
