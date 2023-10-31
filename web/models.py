from django.contrib.auth.models import User

from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.PositiveIntegerField(default=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)


    def __str__(self):
        return self.nome


class Venda(models.Model):
    produto = models.ForeignKey("Produto", on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    data = models.DateTimeField(auto_now_add=True)
    vendedor = models.ForeignKey("auth.User", on_delete=models.CASCADE)  # Adicionando o campo de vendedor

    def __str__(self):
        return f"Venda de {self.quantidade} {self.produto.nome}(s) em {self.data} por {self.vendedor.username}"


class Compra(models.Model):
    produto = models.ForeignKey("Produto", on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Compra de {self.quantidade} {self.produto.nome}(s) em {self.data}"


class CarrinhoDeCompras(models.Model):
    usuario = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    itens = models.ManyToManyField("Produto", through='ItemCarrinho')

    def __str__(self):
        return f'Carrinho de {self.usuario.username}'


class ItemCarrinho(models.Model):
    carrinho = models.ForeignKey(CarrinhoDeCompras, on_delete=models.CASCADE)
    produto = models.ForeignKey("Produto", on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.quantidade} {self.produto.nome}(s) no carrinho'


class Promocao(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    desconto = models.DecimalField(max_digits=5, decimal_places=2)
    produtos = models.ManyToManyField("Produto")

    def __str__(self):
        return self.nome
