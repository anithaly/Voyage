from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # url(r'^$', 'djangoapp.views.home', name='home'),
    url(r'^voyage/', include('voyage.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
