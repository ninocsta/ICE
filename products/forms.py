from django import forms
from django.forms.models import inlineformset_factory
from .models import Product, ProductPrice, PriceTable


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'min_stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'cost': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Nome',
            'description': 'Descrição',
            'min_stock': 'Estoque Mínimo',
            'weight': 'Peso',
            'cost': 'Custo',
        }


class PriceTableForm(forms.ModelForm):
    class Meta:
        model = PriceTable
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Nome',
            'description': 'Descrição',
        }

