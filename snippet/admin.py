from django.contrib import admin
from snippet.models import Snippet
from users.admin import NotForStaff


class SnippetAdmin(NotForStaff):
    fieldsets = (
        (None, {
            'fields': ('name', 'content', 'enabled')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('show_heading', 'html_id', 'html_classes', 'code_mode')
        }),
    )


admin.site.register(Snippet, SnippetAdmin)
