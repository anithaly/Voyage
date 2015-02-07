from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.voyage_list),
    url(r'^(?P<pk>[0-9]+)/$', views.voyage_detail)
)