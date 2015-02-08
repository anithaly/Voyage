from django.conf.urls import patterns, include, url
from . import views

#voyage/
urlpatterns = patterns('',
    url(r'^$', views.voyage_list),
    url(r'^(?P<pk>[0-9]+)/$', views.voyage_detail, name='voyage_list'),
    url(r'^new$', views.voyage_new, name='voyage_new'),
    url(r'^(?P<pk>[0-9]+)/edit$', views.voyage_edit, name='voyage_edit'),
    url(r'^(?P<pk>[0-9]+)/publish$', views.voyage_publish, name='voyage_publish'),
    url(r'^drafts$', views.voyage_draft_list, name='voyage_draft_list'),
    url(r'^(?P<pk>[0-9]+)/remove$', views.voyage_remove, name='voyage_remove'),
)