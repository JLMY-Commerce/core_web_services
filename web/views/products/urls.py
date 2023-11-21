from django.urls import path
from .views import (
    ProdutoListView,
    ProdutoCreateView,
    ProdutoUpdateView,
    ProdutoDeleteView,
)

urlpatterns = [
    path('', ProdutoListView.as_view(), name='produto-list'),
    path('novo/', ProdutoCreateView.as_view(), name='produto-create'),
    path(
        '<int:pk>/',
        ProdutoUpdateView.as_view(),
        name='produto-update'
    ),
    path(
        '<int:pk>/excluir/',
        ProdutoDeleteView.as_view(),
        name='produto-delete'
    ),
]
