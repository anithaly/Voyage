from django.conf.urls import patterns, include, url
from . import views

#place/
urlpatterns = patterns('',
    url(r'^$', views.place_list),
    url(r'^(?P<pk>[0-9]+)/$', views.place_detail, name='place_list'),
    url(r'^new$', views.place_new, name='place_new'),
    url(r'^(?P<pk>[0-9]+)/edit$', views.place_edit, name='place_edit'),
    url(r'^(?P<pk>[0-9]+)/publish$', views.place_publish, name='place_publish'),
    url(r'^drafts$', views.place_drafts_list, name='place_drafts_list'),
    url(r'^(?P<pk>[0-9]+)/remove$', views.place_remove, name='place_remove'),
    url(r'^(?P<pk>[0-9]+)/comment$', views.place_comment_new, name='place_comment_new'),
)