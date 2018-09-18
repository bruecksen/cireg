from django.db import models
from django.db.models import Case, When, Value, IntegerField
from django.utils.translation import gettext as _
from django import forms

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.tags import ClusterTaggableManager
from wagtailtrans.models import TranslatablePage
from taggit.models import TaggedItemBase, Tag as TaggitTag

from wagtail.core.models import Page
from wagtail.core import blocks
from wagtail.snippets.models import register_snippet
from wagtail.core.fields import StreamField, RichTextField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel, InlinePanel, FieldRowPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.documents.edit_handlers import DocumentChooserPanel

from cireg.cms.blocks import PAGE_BLOCKS, CASE_STUDY_BLOCKS


class HomePage(TranslatablePage, Page):
    parent_page_types = ['wagtailtrans.TranslatableSiteRootPage']

    hero_text = RichTextField()
    hero_page_link = models.ForeignKey(
        'wagtailcore.Page',
        verbose_name="Page link",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    hero_page_link_text = models.CharField(max_length=500, verbose_name="Button text", default="Learn more about CIREG")

    project_diary_count = models.PositiveIntegerField(default=3)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            InlinePanel('image_items', label="Hero images"),
            FieldPanel('hero_text'),
            PageChooserPanel('hero_page_link'),
            FieldPanel('hero_page_link_text'),
        ], heading="Hero"),
        FieldPanel('project_diary_count'),
    ]
    template = 'pages/home_page.html'

    def get_context(self, request):
        context = super().get_context(request)
        project_diary_entries = ProjectDiaryEntry.objects.live().annotate(
            is_pinned_post=Case(
                When(pinned_post=True, then=Value(1)),
                default=Value(0),
                output_field=IntegerField())
        )
        project_diary_entries = project_diary_entries.order_by('-is_pinned_post', '-first_published_at')[:3]
        context['project_diary_entries'] = project_diary_entries
        context['case_studies'] = CaseStudy.objects.live()
        return context


class HomePageImageItem(models.Model):
    image = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE,)
    page = ParentalKey('HomePage', related_name='image_items')

    panels = [
        ImageChooserPanel('image'),
    ]


class ProjectDiaryOverview(TranslatablePage, Page):
    parent_page_types = ['cms.HomePage', 'cms.ContentPage']
    template = 'pages/project_diary_overview.html'

    def get_context(self, request):
        context = super().get_context(request)
        entries = ProjectDiaryEntry.objects.child_of(self).live()
        # Filter by tag
        tag = request.GET.get('tag')
        if tag:
            entries = entries.filter(tags__name=tag)
        context['project_diary_entries'] = entries
        return context


class ProjectDiaryTag(TaggedItemBase):
    content_object = ParentalKey('ProjectDiaryEntry', on_delete=models.CASCADE, related_name='entry_tags')


class ProjectDiaryEntry(TranslatablePage, Page):
    parent_page_types = ['cms.ProjectDiaryOverview']

    teaser_image = models.ForeignKey('wagtailimages.Image', on_delete=models.PROTECT, help_text="This image is used for the teaser box at the homepage.")
    teaser_text = models.TextField(help_text="This text is used for the teaser box at the homepage.")
    content = StreamField(PAGE_BLOCKS, null=True, blank=True)
    tags = ClusterTaggableManager(through='ProjectDiaryTag', blank=True)
    pinned_post = models.BooleanField(default=False, help_text="If selected this post will be the first post at the homepage.")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            ImageChooserPanel('teaser_image'),
            FieldPanel('teaser_text')
        ], heading="Teaser"),
        FieldPanel('tags'),
        FieldPanel('pinned_post'),
        StreamFieldPanel('content'),
    ]
    template = 'pages/project_diary_page.html'


class CaseStudy(TranslatablePage, Page):
    parent_page_types = ['cms.ContentPage']

    teaser_image = models.ForeignKey('wagtailimages.Image', on_delete=models.PROTECT, help_text="This image is used for the teaser boxes at the homepage.")
    location = models.CharField(max_length=500)
    highlight_key = models.CharField(max_length=500, null=True, blank=True)
    highlight_value = models.CharField(max_length=500, null=True, blank=True)
    content = StreamField(CASE_STUDY_BLOCKS, null=True, blank=True)

    content_panels = Page.content_panels + [
        ImageChooserPanel('teaser_image'),
        MultiFieldPanel([
            FieldPanel('location'),
            FieldRowPanel([
                FieldPanel('highlight_key'),
                FieldPanel('highlight_value'),
            ]),
        ], heading="Highlight"),
        StreamFieldPanel('content'),
    ]
    template = 'pages/case_study_page.html'


class ContentPage(TranslatablePage, Page):
    parent_page_types = ['cms.HomePage', 'cms.ContentPage']

    content = StreamField(PAGE_BLOCKS, null=True, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('content'),
    ]

    template = 'pages/content_page.html'


TIME_CHOICES = [
    ('historical', _('Historical')),
    ('future', _('Future')),
]


class DownloadOverviewPage(TranslatablePage, Page):
    parent_page_types = ['cms.HomePage', 'cms.ContentPage']

    show_filter = models.BooleanField(default=True)
    intro_text = RichTextField(null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('show_filter'),
        FieldPanel('intro_text'),
    ]
    template = 'pages/download_overview_page.html'

    def get_context(self, request):
        context = super().get_context(request)
        context['energy_type_filter'] = EnergyType.objects.all()
        context['download_items'] = DownloadItem.objects.child_of(self).live()
        return context


class EnergyType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class DownloadItem(Page):
    parent_page_types = ['cms.DownloadOverviewPage']

    description = RichTextField()
    image = models.ForeignKey('wagtailimages.Image', on_delete=models.PROTECT, null=True, blank=True)
    file = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name='+'
    )
    file_text = models.CharField(max_length=500, null=True, blank=True)
    energy_type = ParentalManyToManyField(EnergyType, blank=True)
    timestamp = models.CharField(max_length=20, choices=TIME_CHOICES, null=True, blank=True)


    content_panels = Page.content_panels + [
        FieldPanel('description'),
        ImageChooserPanel('image'),
        MultiFieldPanel([
            DocumentChooserPanel('file'),
            FieldPanel('file_text'),
        ], heading="File"),
        MultiFieldPanel([
            FieldPanel('energy_type', widget=forms.CheckboxSelectMultiple),
            FieldPanel('timestamp', widget=forms.RadioSelect),
        ], heading="Filter")
    ]
    template = 'pages/download_overview_page.html'
