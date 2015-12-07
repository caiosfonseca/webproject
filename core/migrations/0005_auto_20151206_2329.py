# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20151206_2312'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vote',
            old_name='movies',
            new_name='movie',
        ),
    ]
