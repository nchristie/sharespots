# Generated by Django 2.2.10 on 2020-05-22 09:46
from django.contrib.postgres.operations import TrigramExtension
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_venue_image'),
    ]

    operations = [
        TrigramExtension(),
    ]
