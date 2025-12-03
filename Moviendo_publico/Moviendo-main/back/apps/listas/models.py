from django.db import models
from apps.obras.models import Obra


class TipoLista(models.TextChoices):
    PUBLICA = 'publica', 'Pública'
    PRIVADA = 'privada', 'Privada'


class Lista(models.Model):
    nome = models.CharField(max_length=255, verbose_name="Nome")
    descricao = models.TextField(max_length=1000, null=True, blank=True, verbose_name="Descrição")
    tipo = models.CharField(
        max_length=20, 
        choices=TipoLista.choices, 
        default=TipoLista.PUBLICA,
        verbose_name="Tipo"
    )
    obras = models.ManyToManyField(Obra, related_name='listas', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'listas'
        verbose_name = 'Lista'
        verbose_name_plural = 'Listas'
        ordering = ['-created_at']

    def __str__(self):
        return self.nome

    @property
    def total_obras(self):
        return self.obras.count()
