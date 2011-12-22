from django.conf.urls.defaults import patterns, url
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt


urlpatterns = patterns('',
    url(r'^$', csrf_exempt(TemplateView.as_view(template_name='core/home.html')), name='home'),
)

