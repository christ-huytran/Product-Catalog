# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('manufacturer_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'manufacturers',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_name', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('date_added', models.DateField(auto_now_add=True)),
                ('manufacturer', models.ForeignKey(to='product.Manufacturer')),
            ],
            options={
                'db_table': 'products',
            },
        ),
    ]
