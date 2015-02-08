from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', 'djangoapp.views.home', name='home'),
    url(r'^', include('voyage.urls')),
    url(r'^voyage/', include('voyage.urls')),
    url(r'^login$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
                          # {'next_page': '/successfully_logged_out/'}
    ),
    url(r'^admin/', include(admin.site.urls)),
)
