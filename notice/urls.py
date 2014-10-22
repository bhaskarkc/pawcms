from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
                       url(r'^$', views.list_notices, name='list_notices'),
                       url(r'^(?P<slug>[a-zA-Z0-9_.-]+)/$', views.view_notice, name='view_notice'),
)
