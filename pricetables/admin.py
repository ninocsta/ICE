from django.contrib import admin
from .models import PriceTable



class PriceTableAdmin(admin.ModelAdmin):
    list_display = ['table_name','product', 'price']
    search_fields = ['product__title']
    list_filter = ['table_name']

admin.site.register(PriceTable, PriceTableAdmin)