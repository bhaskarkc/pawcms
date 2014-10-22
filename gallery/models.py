from django.db import models


class Album(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    thumbnail = models.ForeignKey('Image', related_name='thumbnail_of')


class Image(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    album = models.ForeignKey(Album)
    file = models.ImageField()