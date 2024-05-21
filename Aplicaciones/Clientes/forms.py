from django import forms

from .models import Nuevo_Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Nuevo_Cliente
        fields = '__all__'