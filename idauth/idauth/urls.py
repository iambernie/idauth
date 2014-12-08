from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    #url(r'^nameless/$', include('nameless.urls', namespace='portal')),
    # Examples:
    # url(r'^$', 'idauth.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    url(r'^terminal/', include('terminal.urls', namespace='terminal')),
    url(r'^nameless/', include('nameless.urls', namespace='loginportal')),
    url(r'^$', include('enlight.urls', namespace='enlight')),
)
