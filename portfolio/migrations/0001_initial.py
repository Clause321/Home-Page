# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import DjangoUeditor.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=127)),
                ('title', models.CharField(max_length=127)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True)),
                ('inprogress', models.BooleanField(default=False)),
                ('abstract', DjangoUeditor.models.UEditorField(verbose_name='content', blank=True)),
                ('detail', DjangoUeditor.models.UEditorField(verbose_name='content', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
