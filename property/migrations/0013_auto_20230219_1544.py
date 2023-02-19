# Generated by Django 2.2.24 on 2023-02-19 12:44

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_auto_20230219_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='owners_pure_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Нормализованный номер владельца'),
        ),
    ]
