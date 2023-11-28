from django.urls import reverse_lazy
from django.views.generic import CreateView

from web.models import Venda
from web.views.vendas.forms import VendaForm


class VenderProdutoView(CreateView):
    model = Venda
    context_object_name = "form"
    template_name = "sales/create.html"
    form_class = VendaForm

    def get_initial(self):
        # Defina os valores iniciais do formulário, se necessário
        initial = super().get_initial()
        initial['vendedor'] = self.request.user
        return initial

    def get_success_url(self):
        return reverse_lazy('produto-list')
