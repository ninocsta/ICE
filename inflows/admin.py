from django.contrib import admin
from .models import Inflow, InflowItem


class InflowItemInline(admin.TabularInline):
    model = InflowItem
    extra = 1
    readonly_fields = ['total_cost']

class InflowAdmin(admin.ModelAdmin):
    inlines = [InflowItemInline]
    list_display = ['pk', 'date', 'total_cost']
    search_fields = ['date']
    date_hierarchy = 'date'
    readonly_fields = ['total_cost']

admin.site.register(Inflow, InflowAdmin)