from django.contrib import admin
from .models import Genero


@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ['nome', 'created_at']
    search_fields = ['nome']
    list_filter = ['created_at']
