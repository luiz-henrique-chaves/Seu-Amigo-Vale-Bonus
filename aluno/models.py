from django.db import models
from curso.models import Curso

class Aluno(models.Model):
    nome_do_aluno = models.CharField(max_length=50)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.CharField(max_length=50)
    matricula = models.CharField(max_length=50)
    id_usuario = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.nome_do_aluno

#example filter
#article = Article.objects.get(pk=1)