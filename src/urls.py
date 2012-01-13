from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from app.profiles.forms import SignupFormExtra

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'', include('app.core.urls', namespace='core')),

    (r'^conta/signup/$', 'userena.views.signup', {'signup_form': SignupFormExtra}),

    (r'^conta/', include('userena.urls')),
    (r'^mensagem/', include('userena.contrib.umessages.urls')),


    # Examples:
    # url(r'^$', 'src.views.home', name='home'),
    # url(r'^src/', include('src.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

     url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
