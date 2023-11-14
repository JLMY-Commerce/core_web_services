from django.views.generic import CreateView

from web.models import Venda
from web.views.vendas.forms import VendaForm


class VenderProdutoView(CreateView):
    model = Venda
    context_object_name = "form"
    template_name = "sales/create.html"
    form_class = VendaForm

