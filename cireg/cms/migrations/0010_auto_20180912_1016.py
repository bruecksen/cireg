# Generated by Django 2.0.8 on 2018-09-12 08:16

import cireg.cms.blocks
from django.db import migrations, models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0009_auto_20180904_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='casestudy',
            name='highlight_key',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='casestudy',
            name='highlight_value',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='casestudy',
            name='location',
            field=models.CharField(default='location', max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='casestudy',
            name='content',
            field=wagtail.core.fields.StreamField([('icon_heading_block', cireg.cms.blocks.IconHeadingBlock()), ('heading_block', cireg.cms.blocks.HeadingBlock()), ('text', wagtail.core.blocks.RichTextBlock()), ('lead_text', cireg.cms.blocks.LeadText()), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('description', wagtail.core.blocks.CharBlock(required=False))])), ('columns_1_1', wagtail.core.blocks.StructBlock([('left_column', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock()), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('description', wagtail.core.blocks.CharBlock(required=False))]))], label='Left')), ('right_column', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock()), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('description', wagtail.core.blocks.CharBlock(required=False))]))], label='Right'))])), ('text_and_fact_block', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.RichTextBlock()), ('facts', wagtail.core.blocks.ListBlock(cireg.cms.blocks.FactBlock))]))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contentpage',
            name='content',
            field=wagtail.core.fields.StreamField([('icon_heading_block', cireg.cms.blocks.IconHeadingBlock()), ('heading_block', cireg.cms.blocks.HeadingBlock()), ('text', wagtail.core.blocks.RichTextBlock()), ('lead_text', cireg.cms.blocks.LeadText()), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('description', wagtail.core.blocks.CharBlock(required=False))])), ('columns_1_1', wagtail.core.blocks.StructBlock([('left_column', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock()), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('description', wagtail.core.blocks.CharBlock(required=False))]))], label='Left')), ('right_column', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock()), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('description', wagtail.core.blocks.CharBlock(required=False))]))], label='Right'))]))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projectdiaryentry',
            name='content',
            field=wagtail.core.fields.StreamField([('icon_heading_block', cireg.cms.blocks.IconHeadingBlock()), ('heading_block', cireg.cms.blocks.HeadingBlock()), ('text', wagtail.core.blocks.RichTextBlock()), ('lead_text', cireg.cms.blocks.LeadText()), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('description', wagtail.core.blocks.CharBlock(required=False))])), ('columns_1_1', wagtail.core.blocks.StructBlock([('left_column', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock()), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('description', wagtail.core.blocks.CharBlock(required=False))]))], label='Left')), ('right_column', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock()), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('description', wagtail.core.blocks.CharBlock(required=False))]))], label='Right'))]))], blank=True, null=True),
        ),
    ]
