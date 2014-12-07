# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0002_slide_keywords'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='front_image',
            field=models.ImageField(default=b'', upload_to=b'image/front/'),
            preserve_default=True,
        ),
    ]
