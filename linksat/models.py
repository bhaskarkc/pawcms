from django.db import models
from froala_editor.fields import FroalaField


class CustomModel(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    image = models.ImageField(upload_to='images/')
    large_image = models.ImageField(upload_to='images/', null=True, blank=True)
    description = FroalaField(null=True, blank=True)
    external_url = models.URLField(null=True, blank=True)

    class Meta:
        abstract = True


class Product(CustomModel):
    pass


class Brand(models.Model):
    pass


class Solution(models.Model):
    pass


class Customer(models.Model):
    pass