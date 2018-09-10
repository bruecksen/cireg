from django import template
from django.template.loader import render_to_string

from cireg.contrib.models import Menu

# from impacts_world.core.models import HeaderSettings
register = template.Library()


def menu_as_context(menu, current_page):
    menu_items = []
    for menu_item in menu.menu_items.all():
        name = menu_item.name
        target = menu_item.target.specific
        target_appendix = menu_item.target_appendix
        if current_page and target == current_page:
            active = True
        else:
            active = False
        children = []
        for child in menu_item.submenu:
            if child.block_type == 'jump_link':
                children.append({'url': '%s%s' % (target.url, child.value.get('link')), 'text': child.value.get('name'), 'is_anchor': True})
            elif child.block_type == 'page_link':
                child_page = child.value.get('page')
                children.append({'url': child_page.url, 'text': child.value.get('name'), 'active': child_page.specific == current_page})
            elif child.block_type == 'external_link':
                children.append({'url': child.value.get('url'), 'text': child.value.get('name'), 'is_external': True})
        if target.url:
            target_url = target.url
            if target_appendix:
                target_url += target_appendix
            menu_items.append({'url': target_url, 'text': name, 'active': active, 'children': children})
    return menu_items


@register.simple_tag(takes_context=True)
def header(context, *args, **kwargs):
    language = context['page'].specific.language
    main_menu = Menu.objects.get(language=language, menu_type=Menu.MAIN_MENU)
    meta_menu = Menu.objects.get(language=language, menu_type=Menu.META_MENU)

    page = context.get('page')

    context['main_menu'] = menu_as_context(main_menu, page)
    context['meta_menu'] = menu_as_context(meta_menu, page)
    context['language'] = language

    translations = page.get_translations(include_self=True)
    context['translations'] = translations
    context.update(kwargs)
    template = 'widgets/header.html'
    return render_to_string(template, context=context.flatten())


@register.simple_tag(takes_context=True)
def footer(context, *args, **kwargs):
    language = context['page'].specific.language
    footer_menu = Menu.objects.get(language=language, menu_type=Menu.FOOTER_MENU)

    page = context.get('page')

    context['footer_menu'] = menu_as_context(footer_menu, page)
    context['language'] = language

    translations = page.get_translations(include_self=True)
    context['translations'] = translations
    context.update(kwargs)
    template = 'widgets/footer.html'
    return render_to_string(template, context=context.flatten())
