# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rgsupport', '0004_department_send_to_chapters'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='resolved',
            field=models.BooleanField(default=False),
        ),
    ]
