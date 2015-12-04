# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='casting',
            field=models.ManyToManyField(to='core.Person', null=True, blank=True, related_name='casting'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='directors',
            field=models.ManyToManyField(to='core.Person', null=True, blank=True, related_name='directors'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='producers',
            field=models.ManyToManyField(to='core.Person', null=True, blank=True, related_name='producerts'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='similars',
            field=models.ManyToManyField(to='core.Movie', null=True, blank=True),
        ),
    ]
