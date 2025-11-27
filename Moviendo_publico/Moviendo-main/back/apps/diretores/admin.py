from django.contrib import admin
from .models import Diretor


@admin.register(Diretor)
class DiretorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'nacionalidade', 'data_nascimento']
    search_fields = ['nome', 'nacionalidade']
    list_filter = ['nacionalidade', 'created_at']
