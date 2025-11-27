from django.contrib import admin
from .models import Avaliacao


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ['obra', 'nota', 'data_avaliacao']
    list_filter = ['nota', 'data_avaliacao']
    search_fields = ['obra__titulo', 'comentario']
    readonly_fields = ['data_avaliacao']
