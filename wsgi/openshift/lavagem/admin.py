from django.contrib import admin
from models import *

class InlineItem(admin.TabularInline):
    model = VendaItem
    raw_id_fields = ('raw_id_fields',)

class AdminVenda(admin.ModelAdmin):
    list_display = ('carro', 'categoria', 'entrada', 'saida', 'km', 'status', 'funInterior', 'funExterior',)
    search_fields = ['carro_placa',]
    list_filtes = ('status',)
    excludes = ('saida', 'status',)
    inlines = [InlineItem

admin.site.register(Venda, AdminVenda)