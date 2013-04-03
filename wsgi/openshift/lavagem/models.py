from django.db import models
from django.contrib.auth.models import User
from cadastro.models import Carro, Categoria, Produto

ST_ENTRADA = 'F'
ST_INTERNO = 'I'
ST_EXTERNO = 'E'
ST_LIBERADO = 'L'
ST_PRONTO = 'P'

STATUS_CHOICES = (
    (ST_ENTRADA, 'Na Fila'),
    (ST_EXTERNO, 'Lavagem Externa'),
    (ST_INTERNO, 'Lavagem Interna'),
    (ST_LIBERADO, 'Aguardando Entraga'),
    (ST_PRONTO, 'Carro Entrege'),
)

class Venda(models.Model):
    funInterior = models.ForeignKey(User, verbose_name='Funcionario Interior', on_delete=models.DO_NOTHING, related_name='fk_venda_user_int')
    funExterior = models.ForeignKey(User, verbose_name='Funcionario Exterior', on_delete=models.DO_NOTHING, related_name='fk_venda_user_ext')
    carro = models.ForeignKey(Carro, verbose_name='Carro', on_delete=models.DO_NOTHING)
    categoria = models.ForeignKey(Categoria, verbose_name='Categoria', on_delete=models.DO_NOTHING)
    entrada = models.DateTimeField(auto_now=False, verbose_name='Entrada')
    saida = models.DateTimeField(verbose_name='Saida', null=True)
    km = models.DecimalField(max_digits=16, decimal_places=2, verbose_name='Quilometragem')
    status = models.CharField(max_length=1, verbose_name='Status', choices=STATUS_CHOICES, default=ST_ENTRADA)
	
    def __unicode__(self):
        return self.carro.placa

class VendaItem(models.Model):
    venda = models.ForeignKey(Venda, verbose_name='Venda', on_delete=models.DO_NOTHING)
    produto = models.ForeignKey(Produto, verbose_name='Produto', on_delete=models.DO_NOTHING)
    qtd = models.IntegerField(verbose_name='Quandidade')
    valor = models.DecimalField(max_digits=16, decimal_places=2, verbose_name='Valor')
	
    def __unicode__(self):
        return self.produto.nome


class Fila(Venda):	
	class Meta:
		proxy = True