from django.http import QueryDict
from django.template import Library
from django.utils.safestring import mark_safe
from ..models import Snippet

register = Library()


@register.filter
def snippet(name, args=''):
    qs = QueryDict(args).copy()

    try:
        snip = Snippet.objects.get(name=name)

        if not snip.enabled:
            return ''

        # write classes
        classes = snip.default_classes()
        if snip.html_classes:
            classes += ' ' + snip.html_classes
        if 'class' in qs:
            classes += ' ' + qs.pop('class')[0]
        content = '<div class="' + classes + '"'

        # write id
        html_id = None
        if snip.html_id:
            html_id = snip.html_id
        if 'id' in qs:
            html_id = qs.pop('id')[0]
        if html_id:
            content += ' id="' + html_id + '"'

        # write other attributes
        for attr in qs:
            content += ' ' + attr + '="' + qs[attr][0] + '"'

        content += '>\n'

        if snip.show_heading:
            content += '\t\t<div class="snippet-heading">' + name + '</div>\n'

        content += '\t\t<div class="snippet-content">\n\t\t\t'

        snip_content = snip.content

        if not snip.code_mode:
            snip_content = snip_content.replace('\n', '<br>')

        content += snip_content

        content += '\n\t\t</div>'

        content += '\n\t</div>'
        return mark_safe(content)

    except Snippet.DoesNotExist:
        return mark_safe('<div class="error">No snippets with name "' + name + '".</div>')