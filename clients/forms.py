from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'cpfcnpj': forms.TextInput(attrs={'class': 'form-control'}), 
            'fone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
           
        }
        labels = {
            'name': 'Nome',
            'cpfcnpj': 'CPF/CNPJ',
            'fone': 'Telefone',
            'address': 'Endereço',
            'city': 'Cidade',

        }