from django.shortcuts import render
from django.views.generic import ListView
from stock.models import Stock
from outflows.models import Outflow
from django.db.models import Sum, F, Q

class StockListView(ListView):
    template_name = 'stock.html'
    context_object_name = 'stock'
    model = Stock
    paginate_by = 10



