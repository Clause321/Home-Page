# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_auto_20141201_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='langs',
            field=models.ManyToManyField(to='portfolio.Lang', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='team',
            field=models.ManyToManyField(to='portfolio.Team', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='tech',
            field=models.ManyToManyField(to='portfolio.Tech', blank=True),
            preserve_default=True,
        ),
    ]
