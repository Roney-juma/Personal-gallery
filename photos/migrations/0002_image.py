# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2021-07-04 20:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='articles/')),
                ('image_name', models.CharField(max_length=30)),
                ('image_description', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('image_category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='photos.Category')),
                ('image_location', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='photos.Location')),
            ],
        ),
    ]