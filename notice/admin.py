from django.contrib import admin
from notice.models import Notice


class NoticeAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    list_display = ('title', 'date')


admin.site.register(Notice, NoticeAdmin)
