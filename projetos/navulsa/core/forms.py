#-*- coding: utf-8 -*-
from django import forms
from models import Pessoa


class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa

    def __init__(self, *args, **kwargs):
        super(PessoaForm, self).__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs = {'class': 'form-control'}
