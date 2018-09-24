# Generated by Django 2.0.8 on 2018-10-16 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('address_1', models.CharField(max_length=150)),
                ('address_2', models.CharField(max_length=150)),
                ('post_code', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=1000)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]