from django.contrib import admin
from .models import Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cor', 'created_at']
    search_fields = ['nome']
    list_filter = ['created_at']
