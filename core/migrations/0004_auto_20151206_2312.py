# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_movie_similars_ids'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='status',
            field=models.CharField(max_length=7, choices=[('dislike', 'Dislike'), ('like', 'Like')]),
        ),
    ]
