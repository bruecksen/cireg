# Generated by Django 2.0.8 on 2018-09-04 11:22

import cireg.cms.blocks
from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('wagtailtrans', '0007_auto_20180327_1127'),
        ('cms', '0006_auto_20180904_1318'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='wagtailcore.Page')),
                ('translatablepage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailtrans.TranslatablePage')),
                ('content', wagtail.core.fields.StreamField([('text', wagtail.core.blocks.RichTextBlock()), ('icon_heading_block', cireg.cms.blocks.IconHeadingBlock()), ('heading_block', cireg.cms.blocks.HeadingBlock())], blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailtrans.translatablepage', 'wagtailcore.page'),
        ),
    ]
