from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^members/', include('app.members.urls')),
    url(r'^payment/', include('app.payment.urls')),


    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('django.contrib.auth.views',
    url(r'^logout/$', 'logout_then_login'),
    url(r'^login/', 'login'),
    url(r'^password/request/$', 'password_reset'),
    url(r'^password/request/done/$', 'password_reset_done'),
    url(r'^password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'password_reset_confirm'),
    url(r'^password/reset/done/$', 'password_reset_complete'),
    url(r'^password/change/$', 'password_change'),
    url(r'^password/change/done/$', 'password_change_done')
)