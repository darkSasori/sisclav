from django.contrib import admin
from models import Cliente, Contato, Carro

class InlineContato(admin.TabularInline):
	model = Contato

class InlineCarro(admin.TabularInline):
	model = Carro

class AdminCliente(admin.ModelAdmin):
	inlines = [InlineContato, InlineCarro]
	list_display = ('nome', 'cpf', 'rg', 'cidade', 'bairro', 'endereco', 'numero',)
	search_fields = ['nome', 'cpf', 'rg', 'cidade', 'bairro', 'endereco', 'numero']
