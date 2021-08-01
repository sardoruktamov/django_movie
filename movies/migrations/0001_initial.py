# Generated by Django 3.2.4 on 2021-08-01 17:22

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nomi')),
                ('age', models.PositiveSmallIntegerField(default=0, verbose_name='Yosh')),
                ('description', models.TextField(verbose_name='Izox')),
                ('image', models.ImageField(upload_to='actors/')),
            ],
            options={
                'verbose_name': 'Aktyor va rejissior',
                'verbose_name_plural': 'Aktyor va rejissiorlar',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Kategoriya')),
                ('description', models.TextField(verbose_name='Izox')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Kategoriya',
                'verbose_name_plural': 'kategoriyalar',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nomi')),
                ('description', models.TextField(verbose_name='Izox')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Janr',
                'verbose_name_plural': 'Janrlar',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='sarlavha')),
                ('tagline', models.CharField(default='', max_length=100, verbose_name='spogan')),
                ('description', models.TextField(verbose_name='Izox')),
                ('poster', models.ImageField(upload_to='movies/', verbose_name='Poster')),
                ('year', models.PositiveSmallIntegerField(default=2020, verbose_name='ishlab chiqilgan yil')),
                ('country', models.CharField(max_length=30, verbose_name='davlat')),
                ('world_premiere', models.DateField(default=datetime.date(2021, 8, 1), verbose_name='Jaxon primyerasi')),
                ('budget', models.PositiveIntegerField(default=0, help_text="summa do'llorda ko'rsatilgan", verbose_name='Byudjet')),
                ('fees_in_usa', models.PositiveIntegerField(default=0, help_text="summa do'llorda ko'rsatilgan", verbose_name='AQSH tulovlari')),
                ('fees_in_world', models.PositiveIntegerField(default=0, help_text="summa do'llorda ko'rsatilgan", verbose_name='AQSH tulovlari')),
                ('url', models.SlugField(max_length=160, unique=True)),
                ('draft', models.BooleanField(default=False, verbose_name='Qoralama')),
                ('actors', models.ManyToManyField(related_name='film_actor', to='movies.Actor', verbose_name='Aktyor')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movies.category', verbose_name='Kategoriya')),
                ('directors', models.ManyToManyField(related_name='film_director', to='movies.Actor', verbose_name='rejissior')),
                ('genres', models.ManyToManyField(to='movies.Genre', verbose_name='Janr')),
            ],
            options={
                'verbose_name': 'film',
                'verbose_name_plural': 'filmlar',
            },
        ),
        migrations.CreateModel(
            name='RatingStar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.SmallIntegerField(default=0, verbose_name='Yulduzcha')),
            ],
            options={
                'verbose_name': 'reyting yulduzcha',
                'verbose_name_plural': 'reyting yulduzchalari',
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100, verbose_name='Ism')),
                ('text', models.TextField(max_length=5000, verbose_name='Xabar')),
                ('movie', models.ForeignKey(on_delete=django.db.models.fields.CharField, to='movies.movie', verbose_name='kino')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='movies.reviews', verbose_name='Uziniki')),
            ],
            options={
                'verbose_name': 'kurib chiqish',
                'verbose_name_plural': 'kurib chiqishlar',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=15, verbose_name='IP adres')),
                ('movie', models.ForeignKey(on_delete=django.db.models.fields.CharField, to='movies.movie', verbose_name='kino')),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.ratingstar', verbose_name='yulduzcha')),
            ],
            options={
                'verbose_name': 'reyting',
                'verbose_name_plural': 'reytinglar',
            },
        ),
        migrations.CreateModel(
            name='MovieShots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='sarlavha')),
                ('description', models.TextField(verbose_name='Izox')),
                ('image', models.ImageField(upload_to='movie_shots/', verbose_name='rasm')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie', verbose_name='Kino')),
            ],
            options={
                'verbose_name': 'filmdan kadr',
                'verbose_name_plural': 'filmdan kadrlar',
            },
        ),
    ]
