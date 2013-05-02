from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
        # eg: /polls/
        url(r'^$', views.index, name='index'),
        # eg: /polls/25/
        url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
        # eg: /polls/25/results/
        url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
        # eg: /polls/25/vote/
        url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)
