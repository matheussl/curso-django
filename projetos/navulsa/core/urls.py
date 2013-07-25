from django.conf.urls import patterns, url


urlpatterns = patterns('core.views',
    url(r'^cadastrar-pessoa/$', 'cadastra_pessoa', name='cadastrar_pessoa'),
    url(r'^edita-pessoa/(\d+)/$', 'edita_pessoa', name='edita_pessoa'),
    url(r'^exibe-pessoa/(\d+)/$', 'exibe_pessoa', name='exibe_pessoa'),
    url(r'^listar-pessoas/$', 'listar_pessoas', name='listar_pessoas'),
)
