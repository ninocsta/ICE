from django.urls import path
from stock.views import StockListView, StockForecastView



urlpatterns = [
    path('stock/', StockListView.as_view(), name='stock_list'),
    path('stock/forecast/', StockForecastView.as_view(), name='stock_forecast'),

]