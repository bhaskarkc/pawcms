from django.db import models
from froala_editor.fields import FroalaField


class Snippet(models.Model):
    name = models.CharField(max_length=254)
    content = FroalaField(blank=True, null=True)
    enabled = models.BooleanField(default=True)
    show_heading = models.BooleanField(default=False)
    html_id = models.CharField(max_length=254, blank=True, null=True, verbose_name='HTML ID',
                               help_text="Don't use ID if you are using this snippet more than once in a page.")
    html_classes = models.CharField(max_length=254, blank=True, null=True, verbose_name='HTML Classes',
                                    help_text='Space separated class names')
    # code_mode = models.BooleanField(default=False, help_text='Preserves the content as is.')

    def __str__(self):
        return self.name

    def default_classes(self):
        return 'snippet snippet-' + self.name.lower().replace(' ', '-')
