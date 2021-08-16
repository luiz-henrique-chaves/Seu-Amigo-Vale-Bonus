from django import forms
from aluno.models import Aluno

class AlunoForm(forms.ModelForm):
	class Meta:
            model = Aluno
            fields = ['nome_do_aluno','curso', 'periodo','matricula','id_usuario']
            widgets = {'id_usuario': forms.HiddenInput(attrs=None)}
