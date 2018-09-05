from wagtail.core.blocks import StreamBlock, PageChooserBlock, StructBlock, CharBlock, \
    TextBlock, ListBlock, TimeBlock, DateBlock, ChoiceBlock, BooleanBlock, URLBlock, \
    IntegerBlock, RichTextBlock
from wagtail.images.blocks import ImageChooserBlock


class IconHeadingBlock(CharBlock):
    class Meta:
        template = 'blocks/icon_heading_block.html'
        icon = 'fa-header'
        label = 'Heading with icon'


class HeadingBlock(CharBlock):
    class Meta:
        template = 'blocks/heading_block.html'
        icon = 'fa-header'
        label = 'Heading'


class FactBlock(StructBlock):
    fact = CharBlock()
    value = CharBlock()


class TextAndFactsBlock(StructBlock):
    text = RichTextBlock()
    facts = ListBlock(FactBlock)

    class Meta:
        template = 'blocks/text_and_facts_block.html'
        icon = 'fa-columns'
        label = 'Text and facts'


PAGE_BLOCKS = [
    ('icon_heading_block', IconHeadingBlock()),
    ('heading_block', HeadingBlock()),
    ('text', RichTextBlock()),
]

CASE_STUDY_BLOCKS = [
    ('icon_heading_block', IconHeadingBlock()),
    ('heading_block', HeadingBlock()),
    ('text', RichTextBlock()),
    ('intro_text', RichTextBlock()),
    ('text_and_fact_block', TextAndFactsBlock()),
]
