# Generated by Django 2.0.8 on 2018-09-12 10:40

from django.db import migrations


def create_energy_types(apps, schema_editor):
    EnergyType = apps.get_model("cms", "EnergyType")
    EnergyType.objects.bulk_create([
        EnergyType(name='Solar'),
        EnergyType(name='Wind'),
        EnergyType(name='Hydro'),
    ])


def delete_energy_types(apps, schema_editor):
    EnergyType = apps.get_model("cms", "EnergyType")
    EnergyType.objects.filter(name__in=['Solar', 'Wind', 'Hydro']).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_auto_20180912_1239'),
    ]

    operations = [
        migrations.RunPython(create_energy_types, delete_energy_types),
    ]
