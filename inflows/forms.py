from django import forms
from . import models
from django.forms.models import inlineformset_factory
from .models import Inflow, InflowItem
from django.core.exceptions import ValidationError


class InflowForm(forms.ModelForm):
    class Meta:
        model = Inflow
        exclude = ('total_cost',)
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'readonly': True}),            
        }
        labels = {
            'date': 'Data',
            
        }

class InflowItemForm(forms.ModelForm):
    class Meta:
        model = InflowItem
        exclude = ('total_cost',)
        widgets = {
            'inflow': forms.HiddenInput(),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),  
            }
        labels = {
            'product': 'Produto',
            'quantity': 'Quantidade',
        }

        
InflowItemFormSet = inlineformset_factory(Inflow, InflowItem, form=InflowItemForm, extra=1, can_delete=True)
