# Generated by Django 2.2.24 on 2023-02-20 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0024_auto_20230220_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='flats',
            field=models.ManyToManyField(blank=True, related_name='owners', to='property.Flat', verbose_name='Квартиры'),
        ),
    ]