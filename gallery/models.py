import datetime
from django.db import models
from app.libr import unique_slugify


class Album(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(
        max_length=255,
        blank=True,
        null=True,
        help_text='Leave empty/unchanged for default slug.')
    description = models.TextField(blank=True, null=True)
    thumbnail = models.ForeignKey('Image', related_name='thumbnail_of', blank=True, null=True)
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(editable=False)

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail
        return self.images.all()[0]

    def save(self, *args, **kwargs):
        unique_slugify(self, self.title)
        if not self.id:
            self.created_at = datetime.datetime.today()
        self.updated_at = datetime.datetime.today()
        super(Album, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Image(models.Model):
    file = models.ImageField()
    album = models.ForeignKey(Album, related_name='images')
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(editable=False)

    @property
    def file_name(self):
        return self.file.file.name.split('/')[-1:][0]

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = datetime.datetime.today()
        self.updated_at = datetime.datetime.today()
        super(Image, self).save(*args, **kwargs)

    def __str__(self):
        if not self.name:
            return self.file_name
        return self.name
