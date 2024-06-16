from django.urls import path
from .views import create_outflow, OutflowListView, OutflowDetailView, OutflowDeleteView, get_product_stock, OutflowUpdateView, OutflowItemDeleteView, OutflowItemUpdateView, create_item_outflow, OutflowDeliver


urlpatterns = [
    
    path('outflow/create/', create_outflow, name='outflow_create'),
    path('outflow/list/', OutflowListView.as_view(), name='outflow_list'),
    path('outflow/<int:pk>/update/', OutflowUpdateView.as_view(), name='outflow_update'),
    path('outflow/<int:pk>/detail/', OutflowDetailView.as_view(), name='outflow_detail'),
    path('outflow/<int:pk>/delete/', OutflowDeleteView.as_view(), name='outflow_delete'),
    path('outflow/<int:pk>/confirmar_entrega', OutflowDeliver.as_view(), name='outflow_deliver'),
    path('get-product-stock/', get_product_stock, name='get_product_stock'),

    path('outflow-item/<int:outflow_id>/create/', create_item_outflow, name='outflow_item_create'),
    path('outflow-item/<int:pk>/delete/', OutflowItemDeleteView.as_view(), name='outflow_item_delete'),
    path('outflow-item/<int:pk>/update/', OutflowItemUpdateView.as_view(), name='outflow_item_update'),
]