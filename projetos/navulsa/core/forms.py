#-*- coding: utf-8 -*-
from django import forms
from models import Pessoa


class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa

    # def clean_cpf(self):
    #     cpf = self.cleaned_data['cpf']
    #     raise forms.ValidationError('CPF inválido')
