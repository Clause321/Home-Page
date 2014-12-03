# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_tree'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='tree',
            field=models.ForeignKey(blank=True, to='portfolio.Tree', null=True),
            preserve_default=True,
        ),
    ]
