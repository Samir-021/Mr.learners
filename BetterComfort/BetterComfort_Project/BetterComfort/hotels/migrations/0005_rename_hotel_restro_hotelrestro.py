# Generated by Django 5.1.3 on 2024-12-08 02:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0004_rename_hotelandrestro_hotel_restro'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Hotel_Restro',
            new_name='HotelRestro',
        ),
    ]