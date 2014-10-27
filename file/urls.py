from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
                       url(r'^$', views.list_files, name='list_files'),
                       # url(r'^(?P<slug>[a-zA-Z0-9_.-]+)/$', views.view_files, name='view_files'),
)
