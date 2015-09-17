# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homes', '0003_home_img2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='home',
            name='img2',
        ),
    ]
