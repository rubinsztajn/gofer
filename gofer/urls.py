from django.conf.urls import patterns, include, url
from django.conf import settings
from metadata import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'squirrel.views.home', name='home'),
    # url(r'^squirrel/', include('gofer.foo.urls')),
    url(r'^$', views.home, name="Gofer"),
    url(r'^logout/$', views.logout, name="logout"),
    url(r'^record/(?P<record_id>\d+)/$', views.record, name="record"),
    url(r'^export/$', views.export, name="export"),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                 {'document_root': settings.MEDIA_ROOT}),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'gofer/login.html'}),
    url(r'^search/', include('haystack.urls')),


    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),

)
