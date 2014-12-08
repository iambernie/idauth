
from django.conf.urls import patterns, url


#urlpatterns = patterns('',
#    url(r'^$', 'nameless.views.home', name='home'),
#    url(r'^signin$', 'nameless.views.signinpage', name='login'),
#    #url(r'^signin$', 'theloginpage', name='login'),
#)

urlpatterns = patterns('nameless.views',
    #url(r'^$', 'home', name='home'),
    url(r'^signin$', 'signinpage', name='login'),
    url(r'^signout$', 'signoutpage', name='logout'),
    #url(r'^signin$', 'theloginpage', name='login'),
)
