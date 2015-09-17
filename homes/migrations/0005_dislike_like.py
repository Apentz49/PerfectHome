# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homes', '0004_remove_home_img2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dislike',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('home', models.ForeignKey(to='homes.Home')),
                ('user', models.ForeignKey(to='homes.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('home', models.ForeignKey(to='homes.Home')),
                ('user', models.ForeignKey(to='homes.Customer')),
            ],
        ),
    ]
