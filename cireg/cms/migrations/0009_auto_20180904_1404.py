# Generated by Django 2.0.8 on 2018-09-04 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0008_auto_20180904_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectdiaryentry',
            name='teaser_image',
            field=models.ForeignKey(help_text='This image is used for the teaser box at the homepage.', on_delete=django.db.models.deletion.PROTECT, to='wagtailimages.Image'),
        ),
        migrations.AlterField(
            model_name='projectdiaryentry',
            name='teaser_text',
            field=models.TextField(help_text='This text is used for the teaser box at the homepage.'),
        ),
    ]
