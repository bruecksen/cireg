# Generated by Django 2.0.8 on 2018-11-05 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0023_casestudyoverview'),
    ]

    operations = [
        migrations.RenameField(
            model_name='downloadoverviewpage',
            old_name='show_filter',
            new_name='show_energy_type_filter',
        ),
        migrations.AddField(
            model_name='downloadoverviewpage',
            name='show_timestamp_filter',
            field=models.BooleanField(default=True),
        ),
    ]
