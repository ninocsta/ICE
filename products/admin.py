from django.contrib import admin
from .models import Product, PriceTable, ProductPrice



class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'min_stock', 'weight']
    search_fields = ['title', 'description']

class PriceTableAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    search_fields = ['title', 'description']

class ProductPriceAdmin(admin.ModelAdmin):
    list_display = ['product', 'price_table', 'price']
    search_fields = ['product', 'price_table']

admin.site.register(Product)
admin.site.register(PriceTable)
admin.site.register(ProductPrice)


