from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from django.utils import timezone
from polls.models import Poll

urlpatterns = patterns('',
        # eg: /polls/
        url(r'^$',
            ListView.as_view(
                queryset=Poll.objects.filter(pub_date__lte=timezone.now).order_by('-pub_date')[:5],
                context_object_name='latest_poll_list',
                template_name='polls/index.html'),
            name='index'),
        # eg: /polls/25/
        url(r'^(?P<pk>\d+)/$',
            DetailView.as_view(
                model=Poll,
                template_name='polls/detail.html'),
            name='detail'),
        # eg: /polls/25/results/
        url(r'^(?P<pk>\d+)/results/$',
            DetailView.as_view(
                model=Poll,
                template_name='polls/results.html'),
            name='results'),
        # eg: /polls/25/vote/
        url(r'^(?P<poll_id>\d+)/vote/$', 'polls.views.vote', name='vote'),
)
