from django import forms
from indicado.models import Indicado

class IndicadoForm(forms.ModelForm):
	class Meta:
		model = Indicado
		fields = [
                  'nome',
                  'telefone',
                  'curso_pretendido',
                  'email',
                  'bonus',
                  'id_usuario',
            ]
