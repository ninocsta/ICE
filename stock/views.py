from django.shortcuts import render
from django.views.generic import ListView
from stock.models import Stock
from outflows.models import Outflow, OutflowItem
from django.db.models import Sum, F, Q
from django.db import models

class StockListView(ListView):
    template_name = 'stock.html'
    context_object_name = 'stock'
    model = Stock
    paginate_by = 15




class StockForecastView(ListView):
    template_name = 'stock_forecast.html'
    context_object_name = 'stock'
    model = Stock
    paginate_by = 15

    def get_queryset(self):
        # Anotar a QuerySet com a quantidade pendente de cada produto
        queryset = super().get_queryset().annotate(
            pending_quantity=Sum(
                F('product__outflowitem__quantity'),
                filter=Q(product__outflowitem__outflow__status='P'),
                output_field=models.IntegerField()
            )
        )
        return queryset