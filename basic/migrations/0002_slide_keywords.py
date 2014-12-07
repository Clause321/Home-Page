# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='keywords',
            field=models.CharField(default=b'', max_length=127),
            preserve_default=True,
        ),
    ]
