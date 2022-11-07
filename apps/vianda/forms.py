from django import forms
from apps.vianda.models import Vianda

class ViandaForm(forms.ModelForm):
    class Meta:
        model = Vianda
        fields = ('frecuencia','tipo_menu','fecha_vianda','cantidad','estado','tipo_plato','user')
        prefix='vianda'

        widgets = {
            'frecha_vianda': forms.TextInput(attrs={'name':'fecha_vianda', 'type':'date'}),
            'cantidad': forms.NumberInput(attrs={'name':'cantidad', 'type':'number', 'min':'1'}),
        }