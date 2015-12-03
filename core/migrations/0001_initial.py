# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('genre_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('tmdb_id', models.IntegerField(unique=True)),
                ('title', models.CharField(max_length=255)),
                ('overview', models.TextField()),
                ('release_date', models.DateField()),
                ('popularity', models.DecimalField(max_digits=4, decimal_places=2)),
                ('poster_path', models.URLField()),
                ('vote_count', models.IntegerField()),
                ('vote_average', models.DecimalField(max_digits=4, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('tmdb_id', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=255)),
                ('job', models.IntegerField(choices=[(0, 'actor'), (1, 'director'), (3, 'producer')])),
                ('nickname', models.CharField(max_length=255)),
                ('biography', models.TextField(null=True, blank=True)),
                ('birthday', models.DateField()),
                ('deathday', models.DateField(null=True, blank=True)),
                ('place_of_birth', models.CharField(max_length=255)),
                ('popularity', models.DecimalField(max_digits=4, decimal_places=2)),
                ('profile_path', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('status', models.IntegerField(choices=[(0, 'unlike'), (1, 'like')])),
                ('movies', models.ForeignKey(to='core.Movie')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='casting',
            field=models.ManyToManyField(to='core.Person', related_name='casting'),
        ),
        migrations.AddField(
            model_name='movie',
            name='directors',
            field=models.ManyToManyField(to='core.Person', related_name='directors'),
        ),
        migrations.AddField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(to='core.Genre'),
        ),
        migrations.AddField(
            model_name='movie',
            name='producers',
            field=models.ManyToManyField(to='core.Person', related_name='producerts'),
        ),
        migrations.AddField(
            model_name='movie',
            name='similars',
            field=models.ManyToManyField(to='core.Movie'),
        ),
    ]
