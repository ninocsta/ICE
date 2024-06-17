from django.shortcuts import render
from django.views.generic import ListView
from stock.models import Stock
from outflows.models import Outflow
from django.db.models import Sum, F, Q

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
        queryset = super().get_queryset()
        queryset = queryset.annotate(
            pending_outflows=Sum(
                F('product__outflowitem__quantity'),
                filter=Q(product__outflowitem__outflow__status='P')
            )
        ).annotate(
            forecasted_stock=F('quantity') - F('pending_outflows')
        )
        return queryset