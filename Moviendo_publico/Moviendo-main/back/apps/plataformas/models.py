from django.db import models


class Plataforma(models.Model):
    nome = models.CharField(max_length=100, unique=True, verbose_name="Nome")
    url = models.URLField(null=True, blank=True, verbose_name="URL")
    logo_url = models.URLField(null=True, blank=True, verbose_name="Logo URL")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'plataformas'
        verbose_name = 'Plataforma'
        verbose_name_plural = 'Plataformas'
        ordering = ['nome']

    def __str__(self):
        return self.nome
