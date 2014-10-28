import os
from django.template.loader import BaseLoader, TemplateDoesNotExist
from core import settings as core_settings
from django.conf import settings
from django.utils._os import safe_join


class Loader(BaseLoader):
    # is_usable = True
    #
    # def get_template_sources(self, template_name):
    # template_dirs = settings.TEMPLATE_DIRS
    # for template_dir in template_dirs:
    # new_dir = os.path.join(template_dir, self.theme)
    # try:
    # yield safe_join(new_dir, template_name)
    # except UnicodeDecodeError:
    #             raise
    #         except ValueError:
    #             pass
    #
    # def load_template_source(self, template_name, template_dirs=None):
    #     tried = []
    #     print 'hey'
    #     self.theme = core_settings.theme
    #     for filepath in self.get_template_sources(template_name):
    #         try:
    #             with open(filepath, 'rb') as fp:
    #                 return (fp.read().decode(settings.FILE_CHARSET), filepath)
    #         except IOError:
    #             tried.append(filepath)
    #     if tried:
    #         error_msg = "Tried %s" % tried
    #     else:
    #         error_msg = "Your TEMPLATE_DIRS setting is empty. Change it to point to at least one template directory."
    #     raise TemplateDoesNotExist(error_msg)
    #
    # load_template_source.is_usable = True

    is_usable = True

    def get_template_source(self, template_name):
        # template_dir = settings.TEMPLATE_DIRS[0]
        return '/home/xtranophilist/pro/paw/app/templates/base2013/base.html'
        # for template_dir in template_dirs:
        #     new_path = os.path.join(template_dir, self.theme, template_name)
        #     print new_path
        #     try:
        #         yield new_path
        #     except UnicodeDecodeError:
        #         raise
        #     except ValueError:
        #         pass

    def load_template_source(self, template_name, template_dirs=None):
        tried = []
        self.theme = core_settings.theme
        print 'bye'
        # for filepath in self.get_template_sources(template_name, template_dirs):
        filepath = self.get_template_source(template_name)
        try:
            with open(filepath, 'rb') as fp:
                return (fp.read().decode(settings.FILE_CHARSET), filepath)
        except IOError:
            tried.append(filepath)
        if tried:
            error_msg = "Tried %s" % tried
        else:
            error_msg = "Your TEMPLATE_DIRS setting is empty. Change it to point to at least one template directory."
        raise TemplateDoesNotExist(error_msg)

    load_template_source.is_usable = True

