# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bangon', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='area',
            name='other_information',
            field=models.TextField(null=True, blank=True),
        ),
    ]
