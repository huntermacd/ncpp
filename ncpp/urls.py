from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',   
    url(r'^admin/', include(admin.site.urls)),
    # this url searches for separate urls.py file inside app
    url(r'', include('sighting.urls')),
)
