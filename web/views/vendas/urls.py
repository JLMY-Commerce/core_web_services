from django.urls import path
from .views import *

urlpatterns = [
    path('nova/', VenderProdutoView.as_view(), name='venda-create'),
]
