from django.db import models
from products.models import Product

class PriceTable(models.Model):
    table_name = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='prices')
    price = models.DecimalField(max_digits=10, decimal_places=2)


    class Meta:
        verbose_name = 'Tabela de Preço'
        verbose_name_plural = 'Tabelas de Preço'

    def __str__(self):
        return f'{self.table_name} {self.price}'