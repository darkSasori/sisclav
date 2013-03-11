from django.db import models
from django.contrib.auth.models import User
from cadastro.models import Carro, Categoria

class Venda(models.Model):
    funInterior = models.ForeignKey(User, verbose_name='Funcionario Interior', on_delete=models.DO_NOTHING, related_name='fk_venda_user_int')
    funExterior = models.ForeignKey(User, verbose_name='Funcionario Exterior', on_delete=models.DO_NOTHING, related_name='fk_venda_user_ext')
    carro = models.ForeignKey(Carro, verbose_name='Carro', on_delete=models.DO_NOTHING)
    categoria = models.ForeignKey(Categoria, verbose_name='Categoria', on_delete=models.DO_NOTHING)
    entrada = models.DateTimeField(auto_now=True, verbose_name='Entrada')
    saida = models.DateTimeField(auto_now=True, verbose_name='Saida')
    km = models.DecimalField(max_digits=16, decimal_places=2, verbose_name='Quilometragem')