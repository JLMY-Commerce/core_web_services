from django.contrib.auth.models import User


# Create your models here.

class Cliente(User):
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.first_name


class Seller(Cliente):
    class Meta:
        verbose_name = 'Vendedor'
        verbose_name_plural = 'Vendedores'

    def __str__(self):
        return self.first_name


class Admin(Cliente):
    class Meta:
        verbose_name = 'Administrador'
        verbose_name_plural = 'Administradores'

    # def __str__(self):
    #     return f"{self.username} - {self.get_doble_name()}"
