from django.contrib import admin
from adminsortable.admin import SortableAdminMixin
from .models import SocialLink


class SocialLinkAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('show_icon', 'title', 'show_url', 'enabled',)
    list_editable = ('enabled',)
    list_display_links = ('show_icon', 'title',)

    def show_url(self, obj):
        return '<a target="_blank" href="%s">%s</a>' % (obj.url, obj.url)

    show_url.allow_tags = True
    show_url.short_description = 'URL'

    def show_icon(self, obj):
        return '<img src="%s"/>' % (obj.icon.url)

    show_icon.allow_tags = True
    show_icon.short_description = 'Icon'


admin.site.register(SocialLink, SocialLinkAdmin)
