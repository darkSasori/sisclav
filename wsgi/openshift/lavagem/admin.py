from django.contrib import admin
from models import *

class InlineItem(admin.TabularInline):
    model = VendaItem
    raw_id_fields = ('produto',)

class AdminVenda(admin.ModelAdmin):
    inlines = [InlineItem]
    exclude = ('status',)
    raw_id_fields = ('carro',)
    list_display = ('carro', 'categoria', 'entrada', 'saida', 'km', 'status', 'funInterior', 'funExterior',)
    search_fields = ['carro_placa',]
    list_filtes = ('status',)

admin.site.register(Venda, AdminVenda)