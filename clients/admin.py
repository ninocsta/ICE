from django.contrib import admin
from .models import Client

class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'cpfcnpj', 'fone', 'adress', 'city']
    search_fields = ['name', 'cpfcnpj']

admin.site.register(Client, ClientAdmin)
