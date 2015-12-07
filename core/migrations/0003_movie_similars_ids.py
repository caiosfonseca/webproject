# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20151206_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='similars_ids',
            field=models.TextField(blank=True, null=True),
        ),
    ]
