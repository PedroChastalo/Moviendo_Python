from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from apps.obras.models import Obra


class Avaliacao(models.Model):
    obra = models.ForeignKey(Obra, on_delete=models.CASCADE, related_name='avaliacoes')
    nota = models.DecimalField(
        max_digits=3, 
        decimal_places=1,
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],
        verbose_name="Nota"
    )
    comentario = models.TextField(max_length=2000, null=True, blank=True, verbose_name="Comentário")
    data_avaliacao = models.DateTimeField(auto_now_add=True, verbose_name="Data da Avaliação")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'avaliacoes'
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        ordering = ['-data_avaliacao']
        unique_together = ['obra']

    def __str__(self):
        return f"{self.obra.titulo} - {self.nota}"
