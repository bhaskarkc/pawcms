from django.contrib import admin
from news.models import News


class NewsAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    list_display = ('title', 'date')


admin.site.register(News, NewsAdmin)
