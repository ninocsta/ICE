from django.shortcuts import render
from django.forms import inlineformset_factory
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from .models import Outflow, OutflowItem
from .forms import OutflowForm, OutflowItemForm
from django.urls import reverse_lazy
from django.http import JsonResponse
from products.models import Product





class OutflowListView(ListView):
    model = Outflow
    template_name = 'outflow_list.html'
    context_object_name = 'outflows'
    paginate_by = 10

    def get_queryset(self):
        # Define 'P' como valor padrão para status se não for especificado na URL
        status = self.request.GET.get('status', 'P')
        queryset = super().get_queryset().filter(status=status)
        return queryset



def create_outflow(request):
    outflow_form = OutflowForm()
    outflow_item_formset = inlineformset_factory(Outflow, OutflowItem, form=OutflowItemForm, extra=1, min_num=1, validate_min=True, can_delete=True)

    if request.method == 'POST':
        forms = OutflowForm(request.POST, prefix='outflow_form')
        formset = outflow_item_formset(request.POST, prefix='outflow_item_formset')

        if forms.is_valid() and formset.is_valid():
            created_outflow = forms.save()
            formset.instance = created_outflow  # Atribui a instância de Outflow corretamente ao formset
            formset.save()
            return redirect('outflow_list')
    else:
        forms = OutflowForm(prefix='outflow_form')
        formset = outflow_item_formset(prefix='outflow_item_formset')

    context = {
        'forms': forms,
        'formset': formset,
    }

    return render(request, 'outflow_create.html', context)


class OutflowDetailView(DetailView):
    model = Outflow
    template_name = 'outflow_detail.html'
    context_object_name = 'outflow'


class OutflowDeleteView(DeleteView):
    model = Outflow
    template_name = 'outflow_delete.html'
    context_object_name = 'outflow'
    success_url = reverse_lazy('outflow_list')


def get_product_stock(request):
    product_id = request.GET.get('product_id')
    
    product = Product.objects.get(id=product_id)
    stock = product.stock.quantity  # Supondo que `stock` é um campo no modelo `Product`
    print(f'ativamos o stock {stock}')
    return JsonResponse({'stock': stock})


class OutflowUpdateView(UpdateView):
    model = Outflow
    template_name = 'outflow_update.html'
    form_class = OutflowForm
    success_url = reverse_lazy('outflow_list')

