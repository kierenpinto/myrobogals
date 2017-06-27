# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rgsupport', '0006_request_rgchapter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='chapter',
        ),
    ]
