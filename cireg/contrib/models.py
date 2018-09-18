from django.db import models
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from wagtail.snippets.models import register_snippet
from wagtail.core.models import Orderable
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, PageChooserPanel, StreamFieldPanel

from wagtailtrans.models import Language


@register_snippet
class Menu(ClusterableModel):
    MAIN_MENU = 'main_menu'
    META_MENU = 'meta_menu'
    FOOTER_MENU = 'footer_menu'
    MENU_TYPE_CHOICES = [
        (MAIN_MENU, 'Main menu'),
        (META_MENU, 'Meta menu'),
        (FOOTER_MENU, 'Footer menu'),
    ]
    language = models.ForeignKey(Language, related_name='menu', on_delete=models.PROTECT)
    menu_type = models.CharField(choices=MENU_TYPE_CHOICES, max_length=255, default=MAIN_MENU)

    panels = [
        FieldPanel('language'),
        FieldPanel('menu_type'),
        InlinePanel('menu_items', label="Menu items"),
    ]

    def __str__(self):
        return "%s (%s)" % (self.get_menu_type_display(), self.language)


class BaseLinkBlock(blocks.StructBlock):
    """
    Base StructBlock class used to prevent DRY code.
    """
    name = blocks.CharBlock()


class JumpLinkBlock(BaseLinkBlock):
    """
    Block that holds a link to any URL.
    """
    link = blocks.CharBlock()

    class Meta:
        icon = 'fa-link'


class PageLinkBlock(BaseLinkBlock):
    """
    Block that holds a page.
    """
    name = blocks.CharBlock(required=False, help_text="If left empty the title of the page is used")
    page = blocks.PageChooserBlock()

    class Meta:
        icon = 'fa-file-o'


class ExternalLinkBlock(BaseLinkBlock):
    """
    Block that holds a page.
    """
    url = blocks.URLBlock()

    class Meta:
        icon = 'fa-link'


class MenuItem(Orderable, models.Model):
    menu = ParentalKey(Menu, related_name='menu_items', on_delete=models.CASCADE)
    target = models.ForeignKey('wagtailcore.Page', on_delete=models.CASCADE, null=True, blank=True)
    target_appendix = models.CharField(max_length=255, null=True, blank=True, verbose_name='Link appendix', help_text='If needed you could append a string to the url, e.g. a hash.')

    _name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Alt. name',
                             help_text='If left empty, the target\'s title will be used.')
    name = property(lambda self: self._name or self.target.title)
    submenu = StreamField([
        ('page_link', PageLinkBlock()),
        ('jump_link', JumpLinkBlock()),
        ('external_link', ExternalLinkBlock()),
    ], null=True, blank=True)

    panels = [
        PageChooserPanel('target'),
        FieldPanel('target_appendix'),
        FieldPanel('_name'),
        StreamFieldPanel('submenu'),
    ]