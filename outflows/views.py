from django.shortcuts import render
from django.forms import inlineformset_factory
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from .models import Outflow, OutflowItem
from .forms import OutflowForm, OutflowItemForm
from django.urls import reverse_lazy
from django.http import JsonResponse
from products.models import Product
from django.urls import reverse
from stock.models import Stock





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



class OutflowItemDeleteView(DeleteView):
    model = OutflowItem
    template_name = 'outflow_item_delete.html'
    context_object_name = 'outflow_item'
    def get_success_url(self):
        # Obtemos o ID do Outflow associado ao OutflowItem que está sendo excluído
        outflow_id = self.object.outflow.id
        # Retornamos a URL para os detalhes desse Outflow
        return reverse_lazy('outflow_detail', kwargs={'pk': outflow_id})


class OutflowItemUpdateView(UpdateView):
    model = OutflowItem
    template_name = 'outflow_item_update.html'
    form_class = OutflowItemForm
    def get_success_url(self):
        # Assumindo que o modelo OutflowItem tem uma chave estrangeira para Outflow chamada 'outflow'
        outflow_id = self.object.outflow.id
        return reverse('outflow_detail', kwargs={'pk': outflow_id})


def create_item_outflow(request, outflow_id):
    outflow = Outflow.objects.get(id=outflow_id)
    if request.method == 'POST':
        form = OutflowItemForm(request.POST, outflow_id=outflow)
        if form.is_valid():
            form.save()
            return redirect('outflow_detail', pk=outflow_id)
    else:
        form = OutflowItemForm(outflow_id=outflow_id)
    context = {
        'form': form,
        'outflow': outflow
    }
    return render(request, 'outflow_item_create.html', context)


class OutflowDeliver(UpdateView):
    model = Outflow
    template_name = 'outflow_deliver.html'
    form_class = OutflowForm
    success_url = reverse_lazy('outflow_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        outflow_items = self.object.items.all()

        # Criar um dicionário para rastrear as quantidades ajustadas de estoque
        stock_quantities = {}

        for item in outflow_items:
            product_id = item.product.id
            if product_id not in stock_quantities:
                # Inicializa a quantidade de estoque no dicionário
                stock_quantities[product_id] = item.product.stock.quantity if hasattr(item.product, 'stock') else 0
            # Subtrai a quantidade do item da quantidade de estoque no dicionário
            stock_quantities[product_id] -= item.quantity

        # Ajustar a quantidade restante no estoque no item para uso no template
        for item in outflow_items:
            product_id = item.product.id
            item.quantity_after_outflow = stock_quantities[product_id]
            if item.quantity_after_outflow < 0:
                negative_stock = True

        context['outflow_items'] = outflow_items
        context['negative_stock'] = negative_stock
        return context