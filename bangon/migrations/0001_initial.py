# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('accessibility', models.CharField(max_length=30, choices=[(b'Accessible', b'Accessible'), (b'Hard to access', b'Hard to access'), (b'Inaccessible', b'Inaccessible')])),
                ('population', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('area', models.ForeignKey(related_name='donations', to='bangon.Area')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('count', models.IntegerField()),
                ('is_donation', models.BooleanField(default=False)),
                ('area', models.ForeignKey(related_name='items', blank=True, to='bangon.Area', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='area',
            name='city',
            field=models.ForeignKey(related_name='areas', to='bangon.City'),
        ),
    ]
