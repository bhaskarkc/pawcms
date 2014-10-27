from django.core.urlresolvers import reverse
from django.db import models
from app.libr import unique_slugify
import datetime
from froala_editor.fields import FroalaField


class File(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(
        max_length=255,
        blank=True,
        null=True,
        help_text='Leave empty/unchanged for default slug.')
    content = FroalaField(null=True, blank=True)
    template = models.CharField(max_length=255, blank=True, null=True)
    statuses = (
        ('Published', 'Published'), ('Draft', 'Draft'), ('Trashed', 'Trashed'))
    status = models.CharField(
        max_length=10,
        choices=statuses,
        default='Published')
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        unique_slugify(self, self.title)
        if not self.id:
            self.created_at = datetime.datetime.today()
        self.updated_at = datetime.datetime.today()
        super(File, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('view_file', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title