from django.db import models

# Create your models here.
class Veiculo(models.Model):
	nome = models.CharField(max_length=50, verbose_name='Nome')

	def __unicode__(self):
		return self.nome

class Marca(models.Model):
	nome = models.CharField(max_length=50, verbose_name='Nome')

	def __unicode__(self):
		return self.nome

class Modelo(models.Model):
	veiculo = models.ForeignKey(Veiculo, verbose_name='Veiculo', on_delete=models.DO_NOTHING)
	marca = models.ForeignKey(Marca, verbose_name='Marca', on_delete=models.DO_NOTHING)
	nome = models.CharField(max_length=50, verbose_name='Nome')

	def __unicode__(self):
		return self.nome


class Cliente(models.Model):
	nome = models.CharField(max_length=200, verbose_name='Nome')
	cpf = models.CharField(max_length=14, verbose_name='CNPJ/CPF')
	rg = models.IntegerField(verbose_name='IE/RG')
	cidade = models.CharField(max_length=100, verbose_name='Cidade')
	bairro = models.CharField(max_length=50, verbose_name='Bairro')
	endereco = models.CharField(max_length=255, verbose_name='Endereco')
	numero = models.IntegerField(verbose_name='Numero')

	def __unicode__(self):
		return self.nome

class Contato(models.Model):
	cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)
	nome = models.CharField(max_length=150, verbose_name='Nome')
	email = models.CharField(max_length=150, null=True, blank=True, verbose_name='E-Mail')
	telefone = models.CharField(max_length=12, null=True, blank=True, verbose_name='Telefone')

	def __unicode__(self):
		return self.nome

class Carro(models.Model):
	cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)
	modelo = models.ForeignKey(Modelo, verbose_name='Modelo', on_delete=models.DO_NOTHING)
	cor = models.CharField(max_length=20, verbose_name='Cor')
	placa = models.CharField(max_length=8, verbose_name='Placa')

	def __unicode__(self):
		return self.placa

class Categoria(models.Model):
	nome = models.CharField(max_length=50, verbose_name='Nome')
	valor = models.DecimalField(max_digits=16, decimal_places=2, verbose_name='Valor')

	def __unicode__(self):
		return self.nome

class Produto(models.Model):
	nome = models.CharField(max_length=50, verbose_name='Nome')
	valor = models.DecimalField(max_digits=16, decimal_places=2, verbose_name='Valor')

	def __unicode__(self):
		return self.nome
