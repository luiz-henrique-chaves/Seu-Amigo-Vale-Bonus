from django import forms
from bonus.models import Bonus

class AlunoForm(forms.ModelForm):
	class Meta:
		model = Bonus
		fields = [ 'tipo_de_bonus',  ]
