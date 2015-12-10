# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20151206_2329'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='movie',
            options={'ordering': ['-popularity', '-vote_average']},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['-popularity', 'name']},
        ),
        migrations.AddField(
            model_name='vote',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 12, 10, 0, 13, 50, 866367, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
