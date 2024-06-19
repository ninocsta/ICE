from django import forms
from .models import Outflow, OutflowItem


class OutflowForm(forms.ModelForm):
    class Meta:
        model = Outflow
        exclude = ('total_cost', 'total_price', 'profit', 'status',)
        widgets = {
           'delivery_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
            'client': forms.Select(attrs={'class': 'form-control'}),
            'price_table': forms.Select(attrs={'class': 'form-control'}),
            'observation': forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 100px;'}),
            'discount': forms.NumberInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),            
        }
        labels = {
            'delivery_date': 'Data de Entrega',
            'client': 'Cliente',
            'price_table': 'Tabela de Preço',
            'observation': 'Observação',
            'discount': 'Desconto',
            'status': 'Status',
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['client'].disabled = True
            self.fields['price_table'].disabled = True

class OutflowItemForm(forms.ModelForm):
    class Meta:
        model = OutflowItem
        exclude = ('total_price',)
        widgets = {
            'outflow': forms.HiddenInput(),
            'product': forms.Select(attrs={'class': 'form-control product-select'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),  
            }
        labels = {
            'product': 'Produto',
            'quantity': 'Quantidade',
        }
    def __init__(self, *args, **kwargs):
        outflow_id = kwargs.pop('outflow_id', None)
        super(OutflowItemForm, self).__init__(*args, **kwargs)
        if outflow_id:
            self.fields['outflow'].initial = outflow_id

            
OutflowItemFormSet = forms.inlineformset_factory(Outflow, OutflowItem, form=OutflowItemForm, extra=1, can_delete=True)