# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rgchapter', '0004_auto_20170406_2245'),
        ('rgsupport', '0005_request_resolved'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='rgChapter',
            field=models.ForeignKey(default=1, to='rgchapter.Chapter'),
            preserve_default=False,
        ),
    ]
