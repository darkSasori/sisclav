from django.contrib import admin
from cliente import AdminCliente
from models import *

class AdminModelo(admin.ModelAdmin):
	list_display = ('nome', 'veiculo', 'marca',)
	search_fields = ['nome', 'veiculo__nome', 'marca__nome']

class AdminValor(admin.ModelAdmin):
	list_display = ('nome', 'valor',)
	search_fields = ['nome', 'valor']

class AdminCarro(admin.ModelAdmin):
    list_display = ('placa', 'cor','modelo', 'marca', 'veiculo', 'cliente',)
    search_fields = ['placa', 'cliente__nome', 'modelo__nome', 'modelo__marca__nome', 'modelo__veiculo__nome', 'cor']
    raw_id_fields = ('cliente',)

    def marca(self, model):
        return model.modelo.marca.nome

    def veiculo(self, model):
        return model.modelo.veiculo.nome

admin.site.register(Veiculo)
admin.site.register(Marca)
admin.site.register(Modelo, AdminModelo)
admin.site.register(Cliente, AdminCliente)
admin.site.register(Categoria, AdminValor)
admin.site.register(Produto, AdminValor)
admin.site.register(Carro, AdminCarro)