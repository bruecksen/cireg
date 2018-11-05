from django.urls import reverse

from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from wagtail.core import hooks

from .models import EnergyType


class EnergyTypeAdmin(ModelAdmin):
    model = EnergyType
    menu_label = 'Energy Type'  # ditch this to use verbose_name_plural from model
    menu_icon = 'tag'  # change as required
    menu_order = 400  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    list_display = ('name',)
    search_fields = ('name',)

# Now you just need to register your customised ModelAdmin class with Wagtail
modeladmin_register(EnergyTypeAdmin)
