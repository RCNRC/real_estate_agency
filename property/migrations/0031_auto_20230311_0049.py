# Generated by Django 2.2.24 on 2023-03-10 21:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0030_auto_20230310_0233'),
    ]

    operations = [
        migrations.RenameField(
            model_name='owner',
            old_name='owner',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='owner',
            old_name='owners_phonenumber',
            new_name='phonenumber',
        ),
        migrations.RenameField(
            model_name='owner',
            old_name='owners_pure_phone',
            new_name='pure_phone',
        ),
    ]