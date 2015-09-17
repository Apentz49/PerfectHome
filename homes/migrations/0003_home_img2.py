# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homes', '0002_home_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='img2',
            field=models.CharField(max_length=500, blank=True, null=True),
        ),
    ]
