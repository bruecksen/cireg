# Generated by Django 2.0.8 on 2018-09-12 10:58

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20180912_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='downloaditem',
            name='description',
            field=wagtail.core.fields.RichTextField(),
        ),
    ]
