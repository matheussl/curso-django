from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from core.views import ListaPessoas

urlpatterns = patterns('',
    url(r'^$', 'core.views.lista_pessoas', name='home'),
    url(r'^lista-pessoas/$', ListaPessoas.as_view(), name='lista_pessoas'),
    url(r'^admin/', include(admin.site.urls)),
)
