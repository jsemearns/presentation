# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bangon', '0005_auto_20191103_0756'),
    ]

    operations = [
        migrations.AddField(
            model_name='donationitem',
            name='unit',
            field=models.CharField(default=b'pcs', max_length=100),
        ),
        migrations.AlterField(
            model_name='donationitem',
            name='donation',
            field=models.ForeignKey(related_name='items', blank=True, to='bangon.Donation', null=True),
        ),
    ]
