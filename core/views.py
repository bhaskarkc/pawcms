from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from socket import error as socket_error
from django.contrib.auth.decorators import user_passes_test
from django.utils.translation import ugettext_lazy as _


def home(request):
    return render(request, 'home.html')


def contact(request):
    message = None
    if request.POST:
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        from_email = request.POST.get('email', '')

        if subject and message and from_email:
            try:
                send_mail(subject, message, from_email, ['contact@devchuli.edu.np'])
                message = 'Thank You for the message!'
            except BadHeaderError:
                message = 'Invalid Data Submitted!'
            except socket_error as the_error:
                if the_error.errno != 111:
                    raise the_error
                message = 'Couldn\'t send Email'
        else:
            message = 'Please fill in the required fields!'
            return render(request, 'contact.html', {'message': message})
    return render(request, 'contact.html', {'message': message})


@user_passes_test(lambda u: u.is_superuser)
def clear_cache(request):
    from django.core.cache import cache
    from django.core.urlresolvers import reverse
    from django.http import HttpResponseRedirect
    from django.contrib import messages

    try:
        cache._cache.flush_all()
    except AttributeError:
        pass
    try:
        cache._cache.clear()
    except AttributeError:
        pass
    try:
        cache._expire_info.clear()
    except AttributeError:
        pass

    # django-redis
    try:
        cache.cache.clear()
    except AttributeError:
        pass

    # django-cacheops
    try:
        from cacheops.conf import redis_client

        redis_client.flushdb()
    except ImportError:
        pass

    messages.info(request, "Cache Cleared")
    try:
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    except KeyError:
        return HttpResponseRedirect(reverse("admin:index"))
    return HttpResponseRedirect(reverse("admin:index"))


from sitetree.sitetreeapp import register_dynamic_trees, compose_dynamic_tree
from sitetree.utils import tree, item
from core import contact_settings

contact_tree = (
    tree('contact', 'Contact Tree', (
        item(_('Contact'), 'contact', alias='contact', in_menu=contact_settings.contact_in_nav),
    )),
)

register_dynamic_trees(
    compose_dynamic_tree(contact_tree, target_tree_alias='main-nav-menu'),
    reset_cache=True
)

