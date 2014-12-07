# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_project_tree'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='front_image',
            field=models.ImageField(null=True, upload_to=b'image/front/', blank=True),
            preserve_default=True,
        ),
    ]
