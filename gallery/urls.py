from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
                       url(r'^$', views.list_albums, name='list_albums'),
                       url(r'^image/(?P<pk>[0-9]+)/$', views.view_image, name='view_image'),
                       url(r'^(?P<slug>[a-zA-Z0-9_.-]+)/$', views.view_album, name='view_album'),

)
