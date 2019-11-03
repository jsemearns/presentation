# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bangon', '0004_auto_20191103_0753'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonationItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('count', models.IntegerField(null=True, blank=True)),
                ('donation', models.ForeignKey(related_name='donation_items', blank=True, to='bangon.Donation', null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='item',
            name='count',
        ),
        migrations.RemoveField(
            model_name='item',
            name='donation',
        ),
    ]
