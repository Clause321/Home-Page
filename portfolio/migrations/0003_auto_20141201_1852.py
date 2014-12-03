# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20141201_1851'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='content',
            new_name='detail',
        ),
    ]
