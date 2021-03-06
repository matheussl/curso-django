# Create your views here.
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

from models import Pessoa


@csrf_exempt
def lista_pessoas(request):
    if request.method == 'GET':
        pessoas = Pessoa.objects.all().order_by('nome')
        context = {'pessoas': pessoas}
        return render(request, 'lista_pessoas.html', context)
    else:
        raise Http404


class ListaPessoas(View):
    template_name = 'lista_pessoas.html'

    def get(self, request):
        pessoas = Pessoa.objects.all().order_by('nome')
        context = {'pessoas': pessoas}
        return render(request, 'lista_pessoas.html', context)

    def post(self, request):
        raise Http404
