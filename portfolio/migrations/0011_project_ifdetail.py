# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_remove_project_front_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='ifdetail',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
