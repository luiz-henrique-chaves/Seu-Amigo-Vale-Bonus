from django import forms
from curso.models import Curso

class CursoForm(forms.ModelForm):
	class Meta:
		model = Curso
		fields = ['nome_do_curso', ]
