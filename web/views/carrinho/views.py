from django.contrib.auth.models import User
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from web.models import Produto, CarrinhoDeCompras, ProdutoCarrinho


class CarrinhoDetalhesView(LoginRequiredMixin, UpdateView):
    template_name = 'carrinho/detalhes.html'
    model = CarrinhoDeCompras
    success_url = reverse_lazy("produto-list")
    fields = ("usuario",)
    context_object_name = "carrinho"



class AdicionarAoCarrinhoView(LoginRequiredMixin, View):
    def get(self, request, produto_id, *args, **kwargs):
        produto = get_object_or_404(Produto, pk=produto_id)
        carrinho = CarrinhoDeCompras.objects.get(usuario=request.user)

        if not carrinho:
            carrinho = CarrinhoDeCompras.objects.create(usuario=request.user, estado="0")

        ProdutoCarrinho.objects.create(carrinho=carrinho, produto=produto, quantidade=1)
        return redirect('produto-list')


class RemoverDoCarrinhoView(LoginRequiredMixin, View):
    def get(self, request, produto_id, *args, **kwargs):
        produto_carrinho = get_object_or_404(ProdutoCarrinho, produto__id=produto_id, carrinho__usuario=request.user)
        produto_carrinho.delete()
        return redirect('carrinho_detalhes')
