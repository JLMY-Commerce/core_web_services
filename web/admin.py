from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.db import models

from .models import Categoria, Produto, Compra, Venda, CarrinhoDeCompras, Promocao, ProdutoCarrinho


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria')


@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ('produto', 'quantidade', 'data')
    list_filter = ('produto',)


admin.site.register(Venda)


@admin.register(Promocao)
class PromocaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'desconto')


class ProdutoCarrinhoInline(admin.TabularInline):
    model = ProdutoCarrinho
    extra = 1


@admin.register(ProdutoCarrinho)
class ProdutoCarrinhoAdmin(admin.ModelAdmin):
    list_display = ("carrinho", "produto", "quantidade")


@admin.register(CarrinhoDeCompras)
class CarrinhoDeComprasAdmin(admin.ModelAdmin):
    list_display = ('usuario',)

    # formfield_overrides = {
    #     models.ManyToManyField: {'widget': FilteredSelectMultiple('itens', False)},
    # }

    inlines = [ProdutoCarrinhoInline]
