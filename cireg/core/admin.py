import os

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from .models import User

from publications_bootstrap.models import Publication, Type, PublicationFile
from publications_bootstrap.admin.publicationadmin import PublicationAdmin as _PublicationAdmin

admin.site.register(User, UserAdmin)

admin.site.unregister(Publication)
admin.site.unregister(Type)

class PublicationAdmin(_PublicationAdmin):
    list_display = ('first_author', 'title', 'year', 'journal_or_book_title', 'status', 'get_publication_files')

    def get_publication_files(self, obj):
        links = []
        if obj.publicationfile_set.exists():
            publication_file = obj.publicationfile_set.first()
            return format_html('<a href="{}" target="_blank">{}</a>', publication_file.file.url, os.path.basename(publication_file.file.name))
    get_publication_files.short_description = 'Files'

admin.site.register(Publication, PublicationAdmin)