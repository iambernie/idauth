
from django.conf.urls import patterns, url

urlpatterns = patterns('enlight.views',
    url(r'^$', 'enlight_index', name='index'),
    #url(r'^signin$', 'signinpage', name='login'),
    #url(r'^signout$', 'signoutpage', name='logout'),
    #url(r'^signin$', 'theloginpage', name='login'),
)
