# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-20 07:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('shopstore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.CASCADE, related_name='product_image', to=settings.FILER_IMAGE_MODEL),
        ),
    ]
