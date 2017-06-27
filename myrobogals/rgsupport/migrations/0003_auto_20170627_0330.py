# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rgsupport', '0002_request_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
