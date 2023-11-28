from django.urls import path
from .views import CarrinhoDetalhesView, AdicionarAoCarrinhoView, RemoverDoCarrinhoView

urlpatterns = [
    path('produtos/<int:pk>', CarrinhoDetalhesView.as_view(), name='carrinho_detalhes'),
    path('adicionar/<int:produto_id>/', AdicionarAoCarrinhoView.as_view(), name='adicionar_ao_carrinho'),
    path('remover/<int:produto_id>/', RemoverDoCarrinhoView.as_view(), name='remover_do_carrinho'),
]
