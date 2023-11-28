from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from web.models import Produto, Categoria, Venda
from web.views.products.forms import ProdutoForm



class ProdutoListView(ListView):
    model = Venda
    template_name = 'products/produto_list.html'
    context_object_name = "products"

    def get_queryset(self):
        queryset = Venda.objects.all()

        search = self.request.GET.get('search')
        if search:
            queryset = Venda.objects.filter(produto__nome__icontains=search)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Categoria.objects.all()
        # Adicione mais dados ao contexto conforme necessário
        return context


class ProdutoCreateView(CreateView):
    model = Produto
    template_name = 'products/create.html'
    form_class = ProdutoForm
    success_url = reverse_lazy('venda-create')


class ProdutoUpdateView(UpdateView):
    model = Produto
    template_name = 'products/produto_form.html'
    fields = ['nome', 'descricao', 'estoque']


class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = 'produto_confirm_delete.html'  # Crie este template
    success_url = reverse_lazy('produto-list')  # Redireciona para a lista de produtos após a exclusão
