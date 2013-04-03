from django.contrib import admin
from models import *

class InlineItem(admin.TabularInline):
	model = VendaItem
	raw_id_fields = ('produto',)

class AdminVenda(admin.ModelAdmin):
	inlines = [InlineItem]
	exclude = ('status','saida')
	raw_id_fields = ('carro',)
	list_display = ('carro', 'categoria', 'entrada', 'saida', 'km', 'status', 'funInterior', 'funExterior',)
	search_fields = ['carro_placa',]
	list_filter = ('status',)

class AdminFila(admin.ModelAdmin):
	def has_add_permission(self, model):
		return False
	
	def has_delete_permission(self, model, arg=None):
		return False
	
	def lavagemExterna(self, request, queryset):
		queryset.update(status=ST_EXTERNO)
	lavagemExterna.short_description = 'Em Lavagem Externa'
	
	def lavagemInterna(self, request, queryset):
		queryset.update(status=ST_INTERNO)
	lavagemInterna.short_description = 'Em Lavagem Interna'
	
	def liberado(self, request, queryset):
		queryset.update(status=ST_LIBERADO)
	liberado.short_description = 'Liberado'
	
	def entrege(self, request, queryset):
		#queryset.update(saida=now())
		queryset.update(status=ST_PRONTO)
	entrege.short_description = 'Pronto'
	
	list_display = ('carro', 'categoria', 'entrada', 'saida', 'km', 'status', 'funInterior', 'funExterior',)
	search_fields = ['carro_placa']
	list_filter = ['status']
	actions = [lavagemExterna, lavagemInterna, liberado, entrege]

admin.site.register(Venda, AdminVenda)
admin.site.register(Fila, AdminFila)