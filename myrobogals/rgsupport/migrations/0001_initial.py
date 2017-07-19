# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rgchapter', '0004_auto_20170406_2245'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('send_to_chapters', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Department_Emails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('message', models.TextField(max_length=100)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('resolved', models.BooleanField(default=False)),
                ('chapter', models.ForeignKey(to='rgchapter.Chapter')),
                ('enquiry_type', models.ForeignKey(to='rgsupport.Department')),
            ],
        ),
        migrations.AddField(
            model_name='department',
            name='destination_email',
            field=models.ManyToManyField(to='rgsupport.Department_Emails'),
        ),
    ]
