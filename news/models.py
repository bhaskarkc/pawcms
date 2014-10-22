from django.core.urlresolvers import reverse
from django.db import models
from froala_editor.fields import FroalaField
from users.models import User
from app.libr import unique_slugify, excerpt
import datetime


class News(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(
        max_length=255,
        blank=True,
        null=True,
        help_text='Leave empty/unchanged for default slug.')
    content = FroalaField(null=True, blank=True)
    date = models.DateField(default=datetime.datetime.today())
    author = models.ForeignKey(User, null=True, blank=True)
    statuses = (
        ('Published', 'Published'), ('Draft', 'Draft'), ('Trashed', 'Trashed'))

    status = models.CharField(
        max_length=10,
        choices=statuses,
        default='Published')
    comments_enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        unique_slugify(self, self.title)
        if not self.id:
            self.created_at = datetime.datetime.today()
        self.updated_at = datetime.datetime.today()
        super(News, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    @property
    def excerpt(self):
        return excerpt(self.content)

    def get_absolute_url(self):
        return reverse('view_news', kwargs={'slug': self.slug})

    class Meta:
        verbose_name_plural = 'News'
        get_latest_by = 'date'
