from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Cliente


class ClienteCreateForm(UserCreationForm):
    username = forms.CharField(label="Digite seu nome de usuário")
    first_name = forms.CharField(label="Digite seu nome")
    email = forms.CharField(label="Digite seu e-mail")
    password1 = forms.CharField(label="Digite sua senha")
    password2 = forms.CharField(label="Repita sua senha")

    class Meta:
        model = Cliente
        fields = ('username', 'first_name', 'email', 'password1', 'password2')
