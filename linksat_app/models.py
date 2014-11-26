from django.db import models
from froala_editor.fields import FroalaField


class BaseModel(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    image = models.ImageField(upload_to='images/')
    large_image = models.ImageField(upload_to='images/', null=True, blank=True)
    description = FroalaField(null=True, blank=True)
    external_url = models.URLField(null=True, blank=True)
    enabled = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Product(BaseModel):
    pass


class Brand(BaseModel):
    pass


class Solution(BaseModel):
    pass


class Customer(BaseModel):
    pass