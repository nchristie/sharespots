# Generated by Django 2.2.10 on 2020-05-22 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_remove_venue_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='image',
            field=models.URLField(null=True),
        ),
    ]
