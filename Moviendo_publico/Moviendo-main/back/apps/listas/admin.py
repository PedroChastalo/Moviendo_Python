from django.contrib import admin
from .models import Lista


@admin.register(Lista)
class ListaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'tipo', 'total_obras', 'created_at']
    list_filter = ['tipo', 'created_at']
    search_fields = ['nome', 'descricao']
    filter_horizontal = ['obras']
