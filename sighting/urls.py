from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = patterns('',
	url(r'^login/$', 'django.contrib.auth.views.login'),
	url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
	# index of site maps to view called 'bird_list'
	url(r'^$', views.bird_list, name="bird_list"),
	url(r'^sighting/(?P<bird_name>[\w-]*)$', views.bird_detail, name="bird_detail"),
) 

# while in development, serve images from local dir
if settings.DEBUG == True:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)