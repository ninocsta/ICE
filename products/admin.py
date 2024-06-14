from django.contrib import admin
from .models import Product



class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'min_stock', 'weight']
    search_fields = ['title', 'description']



admin.site.register(Product)


