# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0012_project_side_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='side_image',
            field=models.ImageField(null=True, upload_to=b'image/side/', blank=True),
            preserve_default=True,
        ),
    ]
