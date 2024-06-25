from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Product, PriceTable, ProductPrice
from .forms import ProductForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = context['products']
        price_tables = PriceTable.objects.all()
        context['products_with_prices_info'] = [
            {
                'product': product,
                'has_prices_for_all_price_tables': self.has_prices_for_all_price_tables(product, price_tables)
            }
            for product in products
        ]
        return context

    def has_prices_for_all_price_tables(self, product, price_tables):
        product_prices = product.prices.all()
        price_table_ids = product_prices.values_list('price_table_id', flat=True)
        return all(price_table.id in price_table_ids for price_table in price_tables)



class ProductCreateView(CreateView):
    model = Product
    template_name = 'product_create.html'
    form_class = ProductForm
    success_url = reverse_lazy('product_list')


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product_update.html'
    form_class = ProductForm
    success_url = reverse_lazy('product_list')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            product = context['product']
            context['has_price_tables'] = PriceTable.objects.filter(prices__product=product)
            context['price_tables'] = PriceTable.objects.exclude(prices__product=product)
            context['product_prices'] = ProductPrice.objects.filter(product=product)
            return context


@csrf_exempt
def vincular_preco(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        price_table_id = request.POST.get('price_table_id')
        price = request.POST.get('price')

        product = Product.objects.get(id=product_id)
        price_table = PriceTable.objects.get(id=price_table_id)

        ProductPrice.objects.create(
            product=product,
            price_table=price_table,
            price=price
        )

        return JsonResponse({'status': 'success'})

    return JsonResponse({'status': 'error'}, status=400)