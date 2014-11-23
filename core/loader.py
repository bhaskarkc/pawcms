import os
from django.template.loader import BaseLoader, TemplateDoesNotExist
from core import settings as core_settings
from django.conf import settings
from django.utils._os import safe_join


def calculate_custom_template_dirs():
    theme = core_settings.theme
    if not theme:
        return ()
    template_dirs = settings.TEMPLATE_DIRS
    possible_dirs = []
    for template_dir in template_dirs:
        possible_dirs.append(os.path.join(template_dir, 'themes', theme))
    return tuple(possible_dirs)

# At compile time, cache the directories to search.
custom_template_dirs = calculate_custom_template_dirs()


class ThemeLoader(BaseLoader):
    is_usable = True

    def get_template_sources(self, template_name, template_dirs=None):
        if not template_dirs:
            template_dirs = custom_template_dirs
        for template_dir in template_dirs:
            try:
                yield safe_join(template_dir, template_name)
            except UnicodeDecodeError:
                raise
            except ValueError:
                pass

    def load_template_source(self, template_name, template_dirs=None):
        for filepath in self.get_template_sources(template_name, template_dirs):
            try:
                with open(filepath, 'rb') as fp:
                    return (fp.read().decode(settings.FILE_CHARSET), filepath)
            except IOError:
                pass
        raise TemplateDoesNotExist(template_name)
