# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_project_front_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='front_image',
        ),
    ]
