from django.db import models
from django.contrib.auth.models import User
from cadatro.models import Carro, Categoria

class Venda(models.Model):
    funInterior = models.ForeignKey(User, verbose_name='Funcionario Interior', on_delete=models.DO_NOTHING)
    funExterior = models.ForeignKey(User, verbose_name='Funcionario Exterior', on_delete=models.DO_NOTHING)
    carro = models.ForeignKey(Carro, verbose_name='Carro', on_delete=models.DO_NOTHING)
    categoria = models.ForeignKey(Categoria, verbose_name='Categoria', on_delete=models.DO_NOTHING)
    entrada = models.DateTimeField(auto_now=