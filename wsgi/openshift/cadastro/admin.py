from django.contrib import admin
from cliente import AdminCliente
from models import *

class AdminModelo(admin.ModelAdmin):
	list_display = ('nome', 'veiculo', 'marca')
	search_fields = ['nome', 'veiculo__nome', 'marca__nome']

class AdminValor(admin.ModelAdmin):
	list_display = ('nome', 'valor',)
	search_fields = ['nome', 'valor']

admin.site.register(Veiculo)
admin.site.register(Marca)
admin.site.register(Modelo, AdminModelo)
admin.site.register(Cliente, AdminCliente)
admin.site.register(Categoria, AdminValor)
admin.site.register(Produto, AdminValor)
