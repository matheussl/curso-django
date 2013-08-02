from django.conf.urls import patterns, include, url
from django.contrib import admin
import core

from api import api_v1

admin.autodiscover()

urlpatterns = patterns('',
    url(r'', include('core.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(api_v1.urls)),
)
