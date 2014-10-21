from django.contrib import admin
from snippet.models import Snippet


class NotForStaff(admin.ModelAdmin):
    def has_add_permission(self, request):
        if not request.user.is_admin:
            return False
        return True

    def has_change_permission(self, request, obj=None):
        if not request.user.is_admin:
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        if not request.user.is_admin:
            return False
        return True


class SnippetAdmin(NotForStaff):
    fieldsets = (
        (None, {
            'fields': ('name', 'content', 'enabled')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            # 'fields': ('show_heading', 'html_id', 'html_classes', 'code_mode')
            'fields': ('show_heading', 'html_id', 'html_classes')
        }),
    )


admin.site.register(Snippet, SnippetAdmin)
