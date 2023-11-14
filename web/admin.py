from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.db import models

from .models import Categoria, Produto, Compra, Venda, CarrinhoDeCompras, ItemCarrinho, Promocao


class ItemCarrinhoInline(admin.TabularInline):
    model = ItemCarrinho
    extra = 1


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


@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display = ('produto', 'preco', 'quantidade', 'data', 'vendedor')
    list_filter = ('produto', 'vendedor')


@admin.register(CarrinhoDeCompras)
class CarrinhoDeComprasAdmin(admin.ModelAdmin):
    list_display = ('usuario',)

    formfield_overrides = {
        models.ManyToManyField: {'widget': FilteredSelectMultiple('itens', False)},
    }

    inlines = (ItemCarrinhoInline,)


@admin.register(Promocao)
class PromocaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'desconto')
