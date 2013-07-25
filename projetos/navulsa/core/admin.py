from django.contrib import admin
from models import Pessoa
from forms import PessoaForm


class PessoaAdmin(admin.ModelAdmin):
    form = PessoaForm

admin.site.register(Pessoa, PessoaAdmin)
