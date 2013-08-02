from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core import serializers
from forms import PessoaForm
from models import Pessoa


def cadastra_pessoa(request):
    if request.method == 'GET':
        form = PessoaForm()
        context = {
            'form': form,
        }
        return render(request, 'cadastra_pessoa.html', context, context_instance=RequestContext(request))
    else:
        form = PessoaForm(request.POST)
        if form.is_valid():
            pessoa = form.save()
            return redirect('exibe_pessoa', pessoa.id,)
        else:
            context = {
                'form': form,
            }
            return render(request, 'cadastra_pessoa.html', context_instance=RequestContext(request))


@login_required
def edita_pessoa(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)

    if request.method == 'GET':
        form = PessoaForm(instance=pessoa)
        context = {
            'form': form,
        }
        return render(request, 'edita_pessoa.html', context)
    else:
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            pessoa = form.save()
            return redirect('exibe_pessoa', pessoa.id,)
        else:
            context = {
                'form': form,
            }
            return render(request, 'edita_pessoa.html', context)


def exibe_pessoa(request, id):

    pessoa = get_object_or_404(Pessoa, id=id)
    context = {
        'pessoa': pessoa,
    }
    return render(request, 'exibe_pessoa.html', context)


def listar_pessoas(request):
    pessoas = Pessoa.objects.all().order_by('-nome')
    context = {
        'pessoas': pessoas,
    }
    return render(request, 'listar_pessoas.html', context)



def listar_pessoas_json(request):
    pessoas = Pessoa.objects.all().order_by('-nome')
    context = {
        'pessoas': pessoas,
    }
    response = serializers.serialize("json", pessoas)
    return HttpResponse(response, mimetype='application/json')
