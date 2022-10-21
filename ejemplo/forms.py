from django import forms
from ejemplo.models import Familiar

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=5)


class FamiliarForm(forms.ModelForm):
  
  direccion = forms.CharField(required=False) # <--- Hacer que el campo sea opcional
  
  class Meta:
    model = Familiar
    fields = ['nombre', 'direccion', 'numero_pasaporte']
