from django.contrib import admin
from django.conf import settings
from .models import Aluno

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome_do_aluno', 'curso', 'periodo', 'matricula',)
    search_fields = ('nome_do_aluno', 'matricula')
    #actions = None

    