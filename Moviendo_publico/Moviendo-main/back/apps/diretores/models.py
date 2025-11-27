from django.db import models


class Diretor(models.Model):
    nome = models.CharField(max_length=255, verbose_name="Nome")
    biografia = models.TextField(max_length=2000, null=True, blank=True, verbose_name="Biografia")
    data_nascimento = models.DateField(null=True, blank=True, verbose_name="Data de Nascimento")
    nacionalidade = models.CharField(max_length=100, null=True, blank=True, verbose_name="Nacionalidade")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'diretores'
        verbose_name = 'Diretor'
        verbose_name_plural = 'Diretores'
        ordering = ['nome']

    def __str__(self):
        return self.nome
