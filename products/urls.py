from django.urls import path
from .views import ProductListView, ProductCreateView, ProductUpdateView, ProductDetailView, vincular_preco, ProductDeleteView, PriceTableListView, PriceTableCreateView, PriceTableUpdateView, PriceTableDeleteView, PriceTableDetailView


urlpatterns = [
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('vincular_preco/', vincular_preco, name='vincular_preco'),
    path('price_tables/', PriceTableListView.as_view(), name='price_table_list'),
    path('price_tables/create/', PriceTableCreateView.as_view(), name='price_table_create'),
    path('price_tables/<int:pk>/update/', PriceTableUpdateView.as_view(), name='price_table_update'),
    path('price_tables/<int:pk>/delete/', PriceTableDeleteView.as_view(), name='price_table_delete'),
    path('price_tables/<int:pk>/', PriceTableDetailView.as_view(), name='price_table_detail'),
]