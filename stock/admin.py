from django.contrib import admin
from .models import Stock

class StockAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity', 'average_cost', 'total_cost']
    search_fields = ['product__title']



admin.site.register(Stock, StockAdmin)