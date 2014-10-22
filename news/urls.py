from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
                       url(r'^$', views.list_news, name='list_news'),
)
