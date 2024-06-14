from django.contrib import admin
from .models import Inflow, InflowItem


class InflowItemInline(admin.TabularInline):
    model = InflowItem
    extra = 1

class InflowAdmin(admin.ModelAdmin):
    inlines = [InflowItemInline]
    list_display = ['pk', 'date', 'total_cost']
    search_fields = ['date']

admin.site.register(Inflow, InflowAdmin)