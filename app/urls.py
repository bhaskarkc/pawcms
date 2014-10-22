from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       (r'^settings/', include('dbsettings.urls')),
                       url(r'^news/', include('news.urls')),
                       url(r'^$', 'core.views.home', name='home'),
                       url(r'contact-us/', 'core.views.contact', name='contact'),
                       url(r'^admin/', include(admin.site.urls)),
                       (r'', include('page.urls')),
)
