from django.db import models
from django.db.models import Case, When, Value, IntegerField

from modelcluster.fields import ParentalKey
from modelcluster.tags import ClusterTaggableManager
from wagtailtrans.models import TranslatablePage
from taggit.models import TaggedItemBase, Tag as TaggitTag

from wagtail.core.models import Page
from wagtail.core import blocks
from wagtail.snippets.models import register_snippet
from wagtail.core.fields import StreamField, RichTextField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel, InlinePanel, FieldRowPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel

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
    parent_page_types = ['cms.HomePage']


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
        StreamFieldPanel('content', classname="full"),
    ]


class CaseStudy(TranslatablePage, Page):
    parent_page_types = ['cms.ContentPage']

    teaser_image = models.ForeignKey('wagtailimages.Image', on_delete=models.PROTECT, help_text="This image is used for the teaser boxes at the homepage.")
    content = StreamField(CASE_STUDY_BLOCKS, null=True, blank=True)

    content_panels = Page.content_panels + [
        ImageChooserPanel('teaser_image'),
        StreamFieldPanel('content', classname="full"),
    ]


class ContentPage(TranslatablePage, Page):
    parent_page_types = ['cms.HomePage', 'cms.ContentPage']

    content = StreamField(PAGE_BLOCKS, null=True, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('content', classname="full"),
    ]
