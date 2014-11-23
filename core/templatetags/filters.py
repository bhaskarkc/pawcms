from django.template import Library, Node, TemplateSyntaxError
from django.db.models.loading import get_model


register = Library()


def strip_quotes(string):
    if string is None:
        return None
    if string.startswith('"') and string.endswith('"'):
        string = string[1:-1]

    if string.startswith("'") and string.endswith("'"):
        string = string[1:-1]

    return string


# http://www.b-list.org/weblog/2006/jun/07/django-tips-write-better-template-tags/
class LatestContentNode(Node):
    def __init__(self, model, num, order_by, varname):
        self.num, self.varname, self.order_by = num, varname, strip_quotes(order_by)
        self.model = get_model(*model.split('.'))

    def render(self, context):

        if self.order_by:
            context[self.varname] = self.model._default_manager.all().order_by(self.order_by)[:self.num]
        else:
            context[self.varname] = self.model._default_manager.all()[:self.num]
        return ''


@register.tag
def get_latest(parser, token):
    bits = token.contents.split()
    if len(bits) is 6:
        return LatestContentNode(bits[1], bits[2], bits[3], bits[5])
    elif len(bits) is 5:
        return LatestContentNode(bits[1], bits[2], None, bits[4])
    else:
        raise TemplateSyntaxError, "invalid number of arguments"

