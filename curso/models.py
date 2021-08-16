from django.db import models

class Curso(models.Model):
    nome_do_curso = models.CharField(max_length=100)
    date_created = models.DateField(auto_now_add = True, null=True	)

    def __str__(self):
        return self.nome_do_curso