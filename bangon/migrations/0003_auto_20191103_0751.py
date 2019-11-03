# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bangon', '0002_area_other_information'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='donated_by',
            field=models.CharField(default='justin', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='count',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
