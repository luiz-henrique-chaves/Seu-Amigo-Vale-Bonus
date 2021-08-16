from django.db import models
from bonus.models import Bonus
from curso.models import Curso


class Indicado(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=50)
    curso_pretendido = models.ForeignKey(Curso, on_delete=models.CASCADE)
    email = models.CharField(max_length=150)
    bonus = models.ForeignKey(Bonus, on_delete=models.CASCADE)
    CHOICES = (
        ('Pendente', 'Pendente'),
        ('Matriculado', 'Matriclado'),
    )
    status = models.CharField(max_length=100, choices = CHOICES, default='Pendente')
    id_usuario = models.CharField(max_length=100)

    def __str__(self):
        return self.nome