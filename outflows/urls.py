from django.urls import path
from .views import create_outflow, OutflowListView, OutflowDetailView, OutflowDeleteView, get_product_stock, OutflowUpdateView


urlpatterns = [
    
    path('outflow/create/', create_outflow, name='outflow_create'),
    path('outflow/list/', OutflowListView.as_view(), name='outflow_list'),
    path('outflow/<int:pk>/update/', OutflowUpdateView.as_view(), name='outflow_update'),
    path('outflow/<int:pk>/detail/', OutflowDetailView.as_view(), name='outflow_detail'),
    path('outflow/<int:pk>/delete/', OutflowDeleteView.as_view(), name='outflow_delete'),
    path('get-product-stock/', get_product_stock, name='get_product_stock'),
]