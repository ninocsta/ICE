from django.urls import path
from .views import ProductListView, ProductCreateView, ProductUpdateView, ProductDetailView, vincular_preco


urlpatterns = [
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    #path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('vincular_preco/', vincular_preco, name='vincular_preco'),
]