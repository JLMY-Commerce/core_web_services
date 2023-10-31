from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from web.models import Produto


class ProdutoListView(ListView):
    model = Produto
    template_name = 'products/produto_list.html'  # Crie este template


class ProdutoCreateView(CreateView):
    model = Produto
    template_name = 'produto_form.html'  # Crie este template
    fields = ['nome', 'descricao', 'preco', 'estoque']


class ProdutoUpdateView(UpdateView):
    model = Produto
    template_name = 'produto_form.html'  # Reutilizando o mesmo template do create
    fields = ['nome', 'descricao', 'preco', 'estoque']


class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = 'produto_confirm_delete.html'  # Crie este template
    success_url = reverse_lazy('produto-list')  # Redireciona para a lista de produtos após a exclusão
