from django.contrib import admin
from models import Album, Image

# admin.site.register(Album)
admin.site.register(Image)


class ImageInline(admin.TabularInline):
    model = Image


class AlbumAdmin(admin.ModelAdmin):
    inlines = [ImageInline, ]


admin.site.register(Album, AlbumAdmin)