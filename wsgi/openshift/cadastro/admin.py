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
    list_display = ('placa', 'cor', 'cliente', 'modelo',)
    search_fields = ['placa']
    
    def has_add_permission(self, request):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Veiculo)
admin.site.register(Marca)
admin.site.register(Modelo, AdminModelo)
admin.site.register(Cliente, AdminCliente)
admin.site.register(Categoria, AdminValor)
admin.site.register(Produto, AdminValor)
admin.site.register(Carro, AdminCarro)