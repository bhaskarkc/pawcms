from django.db import models


class SocialLink(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    icon = models.ImageField(upload_to='social_icons/')
    enabled = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ('order',)

    def __unicode__(self):
        return self.title
