# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='img',
            field=models.CharField(blank=True, null=True, max_length=500),
        ),
    ]
