from django import forms
from .models import Traduccion, Busqueda

class TraduccionForm(forms.ModelForm):
    class Meta:
        model = Traduccion
        fields = ['texto_ingles', 'texto_espanol']

class BusquedaForm(forms.ModelForm):
    class Meta:
        model = Busqueda
        fields = ['consulta']

class BusquedaForm(forms.Form):
    palabra_clave = forms.CharField(max_length=100, required=False, label='Palabra clave')