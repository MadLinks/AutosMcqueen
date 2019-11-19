from django import forms

from apps.auto.models import Auto

class AutoForm(forms.ModelForm):

    class Meta:
        model = Auto

        fields = [
            'modelo',
            'color',
            'anno',
            'tipo',
            'persona',
        ]
        labels ={
            'modelo': 'Modelo',
            'color': 'Color',
            'anno': 'Año',
            'tipo': 'Tipo',
            'persona': 'Comprador',

        }
        widgets = {
            'modelo': forms.TextInput(attrs={'class':'form-control'}),
            'color': forms.TextInput(attrs={'class':'form-control'}),
            'anno': forms.TextInput(attrs={'class':'form-control'}),
            'tipo': forms.TextInput(attrs={'class':'form-control'}),
            'persona': forms.Select(attrs={'class':'form-control'}),

        }