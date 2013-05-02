from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TDB_1.views.home', name='home'),
    # url(r'^TDB_1/', include('TDB_1.foo.urls')),
    url(r'^$', 'homepage.views.hello', name='home'),
    url(r'^polls/', include('polls.urls', namespace="polls")),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
