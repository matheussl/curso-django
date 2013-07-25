from django.conf.urls import patterns, include, url
from django.contrib import admin
import core

admin.autodiscover()

urlpatterns = patterns('',
    url(r'', include('core.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
