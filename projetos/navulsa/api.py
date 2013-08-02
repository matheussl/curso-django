# -*- coding: utf-8 -*-

from tastypie.resources import ModelResource
# from tastypie import fields
from tastypie.api import Api
# from tastypie.serializers import Serializer

from core.models import Pessoa


class CustomResource(ModelResource):
    def determine_format(self, request):
        return "application/json"


# Pessoa

class PessoaResource(CustomResource):

    class Meta:
        queryset = Pessoa.objects.all()
        resource_name = 'pessoa'
        list_allowed_methods = ['get',]
        detail_allowed_methods = ['get',]


    def dehydrate_cpf(self, bundle):
        return bundle.obj.cpf.replace('2', 'z')


api_v1 = Api(api_name='v1')
api_v1.register(PessoaResource())

