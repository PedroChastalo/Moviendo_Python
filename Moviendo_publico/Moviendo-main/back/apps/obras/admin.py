from django.contrib import admin
from .models import Obra


@admin.register(Obra)
class ObraAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'tipo', 'status', 'ano_lancamento', 'created_at']
    list_filter = ['tipo', 'status', 'ano_lancamento', 'generos']
    search_fields = ['titulo', 'sinopse']
    filter_horizontal = ['diretores', 'generos', 'plataformas', 'tags']
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('titulo', 'sinopse', 'tipo', 'status')
        }),
        ('Detalhes', {
            'fields': ('ano_lancamento', 'duracao_minutos', 'url_capa')
        }),
        ('Séries', {
            'fields': ('total_temporadas', 'total_episodios', 'temporada_atual', 'episodio_atual'),
            'classes': ('collapse',)
        }),
        ('Relacionamentos', {
            'fields': ('diretores', 'generos', 'plataformas', 'tags')
        }),
        ('Outros', {
            'fields': ('onde_assistir', 'comentario')
        })
    )
