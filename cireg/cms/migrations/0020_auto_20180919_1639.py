# Generated by Django 2.0.8 on 2018-09-19 14:39

import cireg.cms.blocks
from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0019_auto_20180919_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casestudy',
            name='content',
            field=wagtail.core.fields.StreamField([('icon_heading_block', cireg.cms.blocks.IconHeadingBlock()), ('heading_block', cireg.cms.blocks.HeadingBlock()), ('text', wagtail.core.blocks.RichTextBlock()), ('lead_text', cireg.cms.blocks.LeadText()), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('description', wagtail.core.blocks.CharBlock(required=False))])), ('columns_1_1', wagtail.core.blocks.StructBlock([('left_column', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock()), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('description', wagtail.core.blocks.CharBlock(required=False))]))], label='Left')), ('right_column', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock()), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('description', wagtail.core.blocks.CharBlock(required=False))]))], label='Right'))])), ('columns_1_3', wagtail.core.blocks.StructBlock([('left_column', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock()), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('description', wagtail.core.blocks.CharBlock(required=False))]))], label='Left')), ('right_column', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock()), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('description', wagtail.core.blocks.CharBlock(required=False))]))], label='Right'))])), ('columns_4', wagtail.core.blocks.StructBlock([('first', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock()), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('description', wagtail.core.blocks.CharBlock(required=False))]))], label='First')), ('second', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock()), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('description', wagtail.core.blocks.CharBlock(required=False))]))], label='Second')), ('third', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock()), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('description', wagtail.core.blocks.CharBlock(required=False))]))], label='Third')), ('fourth', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock()), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('description', wagtail.core.blocks.CharBlock(required=False))]))], label='Fourth'))])), ('text_and_fact_block', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.RichTextBlock()), ('facts', wagtail.core.blocks.ListBlock(cireg.cms.blocks.FactBlock))]))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contentpage',
            name='content',
            field=wagtail.core.fields.StreamField([('icon_heading_block', cireg.cms.blocks.IconHeadingBlock()), ('heading_block', cireg.cms.blocks.HeadingBlock()), ('text', wagtail.core.blocks.RichTextBlock()), ('lead_text', cireg.cms.blocks.LeadText()), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('description', wagtail.core.blocks.CharBlock(required=False))])), ('columns_1_1', wagtail.core.blocks.StructBlock([('left_column', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock()), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('description', wagtail.core.blocks.CharBlock(required=False))]))], label='Left')), ('right_column', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock()), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('description', wagtail.core.blocks.CharBlock(required=False))]))], label='Right'))])), ('columns_1_3', wagtail.core.blocks.StructBlock([('left_column', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock()), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('description', wagtail.core.blocks.CharBlock(required=False))]))], label='Left')), ('right_column', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock()), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('description', wagtail.core.blocks.CharBlock(required=False))]))], label='Right'))])), ('columns_4', wagtail.core.blocks.StructBlock([('first', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock()), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('description', wagtail.core.blocks.CharBlock(required=False))]))], label='First')), ('second', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock()), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('description', wagtail.core.blocks.CharBlock(required=False))]))], label='Second')), ('third', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock()), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('description', wagtail.core.blocks.CharBlock(required=False))]))], label='Third')), ('fourth', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock()), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('description', wagtail.core.blocks.CharBlock(required=False))]))], label='Fourth'))]))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projectdiaryentry',
            name='content',
            field=wagtail.core.fields.StreamField([('icon_heading_block', cireg.cms.blocks.IconHeadingBlock()), ('heading_block', cireg.cms.blocks.HeadingBlock()), ('text', wagtail.core.blocks.RichTextBlock()), ('lead_text', cireg.cms.blocks.LeadText()), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('description', wagtail.core.blocks.CharBlock(required=False))])), ('columns_1_1', wagtail.core.blocks.StructBlock([('left_column', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock()), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('description', wagtail.core.blocks.CharBlock(required=False))]))], label='Left')), ('right_column', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock()), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('description', wagtail.core.blocks.CharBlock(required=False))]))], label='Right'))])), ('columns_1_3', wagtail.core.blocks.StructBlock([('left_column', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock()), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('description', wagtail.core.blocks.CharBlock(required=False))]))], label='Left')), ('right_column', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock()), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('description', wagtail.core.blocks.CharBlock(required=False))]))], label='Right'))])), ('columns_4', wagtail.core.blocks.StructBlock([('first', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock()), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('description', wagtail.core.blocks.CharBlock(required=False))]))], label='First')), ('second', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock()), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('description', wagtail.core.blocks.CharBlock(required=False))]))], label='Second')), ('third', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock()), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('description', wagtail.core.blocks.CharBlock(required=False))]))], label='Third')), ('fourth', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock()), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('description', wagtail.core.blocks.CharBlock(required=False))]))], label='Fourth'))]))], blank=True, null=True),
        ),
    ]