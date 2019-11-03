# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bangon', '0003_auto_20191103_0751'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='is_donation',
        ),
        migrations.AddField(
            model_name='item',
            name='donation',
            field=models.ForeignKey(related_name='donation_items', blank=True, to='bangon.Donation', null=True),
        ),
    ]
