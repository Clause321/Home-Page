# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import DjangoUeditor.models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20141201_1852'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectLabel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=31)),
                ('iflink', models.BooleanField(default=False)),
                ('link', models.CharField(max_length=127, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Langs',
            fields=[
                ('projectlabel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='portfolio.ProjectLabel')),
            ],
            options={
            },
            bases=('portfolio.projectlabel', models.Model),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('projectlabel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='portfolio.ProjectLabel')),
            ],
            options={
            },
            bases=('portfolio.projectlabel', models.Model),
        ),
        migrations.CreateModel(
            name='Tech',
            fields=[
                ('projectlabel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='portfolio.ProjectLabel')),
            ],
            options={
            },
            bases=('portfolio.projectlabel', models.Model),
        ),
        migrations.AlterField(
            model_name='project',
            name='abstract',
            field=DjangoUeditor.models.UEditorField(verbose_name='abstract', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='detail',
            field=DjangoUeditor.models.UEditorField(verbose_name='detail', blank=True),
            preserve_default=True,
        ),
    ]
