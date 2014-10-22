from django.db import models


class Album(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    thumbnail = models.ForeignKey('Image', related_name='thumbnail_of', blank=True, null=True)

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail
        return self.images.all()[0]

    def __str__(self):
        return self.name


class Image(models.Model):
    file = models.ImageField()
    album = models.ForeignKey(Album, related_name='images')
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    @property
    def file_name(self):
        return self.file.file.name.split('/')[-1:][0]

    def __str__(self):
        if not self.name:
            return self.file_name
        return self.name
