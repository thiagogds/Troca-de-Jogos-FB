from django.conf.urls.defaults import patterns, include, url
from django.http import HttpResponse

urlpatterns = patterns('',
    url(r'^dummy-url/(\w+)/$', lambda request: HttpResponse('absurl'), name='dummy_url'),
)
