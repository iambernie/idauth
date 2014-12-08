
from django.conf.urls import patterns, url

#urlpatterns = patterns('',
#    url(r'^$', 'nameless.views.home', name='home'),
#    url(r'^signin$', 'nameless.views.signinpage', name='login'),
#    #url(r'^signin$', 'theloginpage', name='login'),
#)

urlpatterns = patterns('terminal.views',
    url(r'^$', 'terminalhome', name='home'),
    url(r'^dashboard$', 'terminaldashboard', name='dashboard'),
    #url(r'^signin$', 'signinpage', name='login'),
    #url(r'^signout$', 'signoutpage', name='logout'),
    #url(r'^signin$', 'theloginpage', name='login'),
)
