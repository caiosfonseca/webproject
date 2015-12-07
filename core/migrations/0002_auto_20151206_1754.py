# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='job',
        ),
        migrations.AlterField(
            model_name='person',
            name='birthday',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='nickname',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='place_of_birth',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='popularity',
            field=models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=4),
        ),
    ]
