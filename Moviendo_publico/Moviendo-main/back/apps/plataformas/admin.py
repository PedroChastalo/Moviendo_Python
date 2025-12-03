from django.contrib import admin
from .models import Plataforma


@admin.register(Plataforma)
class PlataformaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'url', 'created_at']
    search_fields = ['nome']
    list_filter = ['created_at']
