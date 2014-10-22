from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
                       url(r'^$', views.list_news, name='list_news'),
                       url(r'^(?P<slug>[a-zA-Z0-9_.-]+)/$', views.view_news, name='view_news'),
)
