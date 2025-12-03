from django.db import models


class Tag(models.Model):
    nome = models.CharField(max_length=50, unique=True, verbose_name="Nome")
    cor = models.CharField(max_length=7, null=True, blank=True, verbose_name="Cor (Hex)")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tags'
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ['nome']

    def __str__(self):
        return self.nome
