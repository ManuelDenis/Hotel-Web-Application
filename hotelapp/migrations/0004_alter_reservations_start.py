# Generated by Django 3.2 on 2023-01-27 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelapp', '0003_alter_reservations_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservations',
            name='start',
            field=models.DateField(),
        ),
    ]
