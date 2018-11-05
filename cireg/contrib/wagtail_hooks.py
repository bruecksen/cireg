from django.urls import reverse

from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from wagtail.core import hooks
from wagtail.admin.menu import MenuItem

from .models import Menu


class MenuModelAdmin(ModelAdmin):
    model = Menu
    menu_label = 'Menu'  # ditch this to use verbose_name_plural from model
    menu_icon = 'fa-list'  # change as required
    menu_order = 400  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view

# Now you just need to register your customised ModelAdmin class with Wagtail
modeladmin_register(MenuModelAdmin)


@hooks.register('construct_main_menu')
def hide_snippets_menu_item(request, menu_items):
    menu_items[:] = [item for item in menu_items if item.name != 'snippets']


@hooks.register('register_admin_menu_item')
def register_publications_menu_item():
    return MenuItem('Publications', reverse('admin:publications_bootstrap_publication_changelist'), classnames='icon icon-folder-inverse', order=10000)

