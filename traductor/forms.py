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
