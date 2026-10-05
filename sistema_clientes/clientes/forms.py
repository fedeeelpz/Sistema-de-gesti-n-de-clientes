from django import forms
from .models import Cliente, Deuda


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre'}),
            'apellido': forms.TextInput(attrs={'placeholder': 'Apellido'}),
        }


class DeudaForm(forms.ModelForm):
    class Meta:
        model = Deuda
        fields = ['monto', 'estado']
        widgets = {
            'monto': forms.NumberInput(attrs={'placeholder': '0.00', 'step': '0.01'}),
        }