from django.urls import path
from .views import create_inflow, InflowListView, InflowDetailView, InflowDeleteView


urlpatterns = [
    
    path('inflows/create/', create_inflow, name='inflow_create'),
    path('inflows/list/', InflowListView.as_view(), name='inflow_list'),
    path('inflows/<int:pk>/detail/', InflowDetailView.as_view(), name='inflow_detail'),
    path('inflows/<int:pk>/delete/', InflowDeleteView.as_view(), name='inflow_delete')
]