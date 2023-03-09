# Generated by Django 2.2.24 on 2023-03-09 23:19

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0027_auto_20230220_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='owner',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='ФИО владельца'),
        ),
        migrations.AddField(
            model_name='owner',
            name='owners_phonenumber',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Номер владельца'),
        ),
        migrations.AddField(
            model_name='owner',
            name='owners_pure_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Нормализованный номер владельца'),
        ),
    ]