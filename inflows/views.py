from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView
from django.forms import inlineformset_factory
from django.shortcuts import render
from .models import Inflow, InflowItem
from .forms import InflowForm, InflowItemForm
from django.shortcuts import redirect





class InflowListView(ListView):
    model = Inflow
    template_name = 'inflow_list.html'
    context_object_name = 'inflows'
    paginate_by = 10






def create_inflow(request):
    inflow_form = InflowForm()
    inflow_item_formset = inlineformset_factory(Inflow, InflowItem, form=InflowItemForm, extra=3, min_num=1, validate_min=True, can_delete=True)

    if request.method == 'POST':
        forms = InflowForm(request.POST, prefix='inflow_form')
        formset = inflow_item_formset(request.POST, prefix='inflow_item_formset')

        if forms.is_valid() and formset.is_valid():
            created_inflow = forms.save()
            formset.instance = created_inflow  # Atribui a instância de Inflow corretamente ao formset
            print(formset.instance)
            formset.save()
            return redirect('inflow_list')
    else:
        forms = InflowForm(prefix='inflow_form')
        formset = inflow_item_formset(prefix='inflow_item_formset')

    context = {
        'forms': forms,
        'formset': formset,
    }

    return render(request, 'inflow_create.html', context)


   
class InflowDetailView(DetailView):
    model = Inflow
    template_name = 'inflow_detail.html'
    context_object_name = 'inflow'


class InflowDeleteView(DeleteView):
    model = Inflow
    template_name = 'inflow_delete.html'
    context_object_name = 'inflow'
    success_url = reverse_lazy('inflow_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        inflow_items_with_stock_and_deletable_flag = []
        product_quantity_needed = {}  # Dicionário para acumular a quantidade necessária por produto

        for item in self.object.items.all():
            item_stock = item.product.stock  # Assumindo que `product` tem um atributo `stock` com um campo `quantity`
            
            # Acumula a quantidade necessária para cada produto
            if item.product.id in product_quantity_needed:
                product_quantity_needed[item.product.id] += item.quantity
            else:
                product_quantity_needed[item.product.id] = item.quantity

            inflow_items_with_stock_and_deletable_flag.append({
                'item': item,
                'stock': item_stock.quantity,  # Certifique-se de que isso é um inteiro representando a quantidade de estoque
            })

        # Verifica se a quantidade necessária de cada produto não excede o estoque
        can_delete = all(
            product_quantity_needed[product_id] <= item['stock']
            for item in inflow_items_with_stock_and_deletable_flag
            for product_id in product_quantity_needed
            if item['item'].product.id == product_id
        )

        context['inflow_items'] = inflow_items_with_stock_and_deletable_flag
        context['can_delete'] = can_delete
        return context