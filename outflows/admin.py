from django.contrib import admin
from .models import Outflow, OutflowItem


class OutflowItemInline(admin.TabularInline):
    model = OutflowItem
    extra = 1
    readonly_fields = ['total_price']

class OutflowAdmin(admin.ModelAdmin):
    inlines = [OutflowItemInline]
    list_display = ['created_at', 'delivery_date', 'client', 'price_table', 'status']
    search_fields = ['client__name', 'price_table__name']
    list_filter = ['status', 'price_table']
    date_hierarchy = 'created_at'
    readonly_fields = ['total_cost', 'total_price', 'profit', ]


admin.site.register(Outflow, OutflowAdmin)