from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.voyage_list),
    url(r'^(?P<pk>[0-9]+)/$', views.voyage_detail),
    url(r'^new$', views.voyage_new, name='voyage_new'),
    url(r'^(?P<pk>[0-9]+)/edit$', views.voyage_edit, name='voyage_edit'),
)