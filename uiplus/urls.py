from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'uiplus.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include ('upload.urls', namespace='upload')),
)

if settings.DEBUG:
  urlpatterns += patterns('',
      (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
  )
