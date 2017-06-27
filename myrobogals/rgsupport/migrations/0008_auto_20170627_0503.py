# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rgsupport', '0007_remove_request_chapter'),
    ]

    operations = [
        migrations.RenameField(
            model_name='request',
            old_name='rgChapter',
            new_name='chapter',
        ),
    ]
