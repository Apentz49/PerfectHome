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
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('address', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=20)),
                ('zipcode', models.CharField(max_length=10)),
                ('bedrooms', models.CharField(max_length=50, blank=True, null=True)),
                ('bathrooms', models.CharField(max_length=100)),
                ('sqft', models.CharField(max_length=12, blank=True, null=True)),
                ('lot_size', models.CharField(blank=True, max_length=50)),
                ('year_built', models.CharField(max_length=5, blank=True, null=True)),
                ('price', models.CharField(max_length=50, null=True)),
                ('price_per_sqft', models.CharField(max_length=10, blank=True, null=True)),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
