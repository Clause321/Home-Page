# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20141201_1940'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Langs',
            new_name='Lang',
        ),
    ]
