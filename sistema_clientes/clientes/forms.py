from django import forms
from .models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'monto', 'estado']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre del cliente'}),
            'monto': forms.NumberInput(attrs={'placeholder': '0.00', 'step': '0.01'}),
            'estado': forms.Select(),
        }