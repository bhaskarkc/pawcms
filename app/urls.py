from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       (r'^admin/settings/', include('dbsettings.urls')),
                       url(r'admin/clear-cache/', 'core.views.clear_cache', name='clear_cache'),
                       url(r'^froala_editor/', include('froala_editor.urls')),

                       url(r'^news/', include('news.urls')),
                       url(r'^notice/', include('notice.urls')),
                       url(r'^gallery/', include('gallery.urls')),
                       url(r'^file/', include('file.urls')),
                       url(r'^$', 'core.views.home', name='home'),
                       url(r'contact-us/', 'core.views.contact', name='contact'),
                       url(r'apply-online/', 'college.views.apply_online', name='apply_online'),
                       url(r'^admin/', include(admin.site.urls)),
                       (r'', include('page.urls')),
)
