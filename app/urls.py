from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.views.generic.base import RedirectView
from .views import dashboard, get_data

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='dashboard/')),
    path('dashboard/', dashboard, name='dashboard'),
    path('data/', get_data, name='data'),
    path('', include('inflows.urls')),
    path('', include('outflows.urls')),
    path('', include('stock.urls')),
    path('', include('products.urls')),
]
