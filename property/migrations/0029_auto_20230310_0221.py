# Generated by Django 2.2.24 on 2023-03-09 23:21

from django.db import migrations


def autocomplete_owners(apps, schema_editor):
    Owner = apps.get_model('property', 'Owner')
    Flat = apps.get_model('property', 'Flat')
    flats_set = Flat.objects.all()
    for flat in flats_set.iterator():
        owner, _ = Owner.objects.get_or_create(
            owner=flat.owner,
            owners_phonenumber=flat.owners_phonenumber,
            owners_pure_phone=flat.owners_pure_phone,
        )
        owner.flats.add(flat)
        owner.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0028_auto_20230310_0219'),
    ]

    operations = [
        migrations.RunPython(autocomplete_owners),
    ]
