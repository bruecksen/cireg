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


class LeadText(RichTextBlock):
    class Meta:
        template = 'blocks/lead_text.html'


class ImageBlock(StructBlock):
    image = ImageChooserBlock()
    description = CharBlock(required=False)

    class Meta:
        template = 'blocks/image_block.html'
        label = 'Image'
        icon = 'fa-image'


COLUMNS_BLOCKS = [
    ('text', RichTextBlock()),
    ('image_block', ImageBlock()),
]


class ColumnsBlock(StructBlock):
    left_column = StreamBlock(COLUMNS_BLOCKS, label="Left")
    right_column = StreamBlock(COLUMNS_BLOCKS, label="Right")

    def get_context(self, value, parent_context=None):
        context = super(ColumnsBlock, self).get_context(value, parent_context=parent_context)
        context['left_column'] = value.get('left_column')
        context['right_column'] = value.get('right_column')
        return context

    class Meta:
        icon = 'table'
        label = 'Columns 1-1'
        template = None


class Columns1To1Block(ColumnsBlock):
    class Meta:
        label = 'Columns [1|1]'
        template = 'blocks/columns-1-1.html'


class Columns1To3Block(ColumnsBlock):
    class Meta:
        label = 'Columns [1|3]'
        template = 'blocks/columns-1-3.html'


class FourColumnsBlock(StructBlock):
    first = StreamBlock(COLUMNS_BLOCKS, label="First")
    second = StreamBlock(COLUMNS_BLOCKS, label="Second")
    third = StreamBlock(COLUMNS_BLOCKS, label="Third")
    fourth = StreamBlock(COLUMNS_BLOCKS, label="Fourth")

    class Meta:
        icon = 'table'
        label = 'Columns [1|1|1|1]'
        template = 'blocks/columns-4.html'


BASE_BLOCKS = [
    ('icon_heading_block', IconHeadingBlock()),
    ('heading_block', HeadingBlock()),
    ('text', RichTextBlock()),
    ('lead_text', LeadText()),
    ('image_block', ImageBlock()),
    ('columns_1_1', Columns1To1Block()),
    ('columns_1_3', Columns1To3Block()),
    ('columns_4', FourColumnsBlock()),
]

PAGE_BLOCKS = BASE_BLOCKS + [
]

CASE_STUDY_BLOCKS = BASE_BLOCKS + [
    ('text_and_fact_block', TextAndFactsBlock()),
]
