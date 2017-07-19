# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rgsupport', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='date_resolved',
            field=models.DateTimeField(null=True),
        ),
    ]
