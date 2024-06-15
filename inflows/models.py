from django.db import models
from products.models import Product



class Inflow(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'
        ordering = ['-date']

    def get_total_cost(self):
        return sum(item.total_cost for item in self.items.all())
    

    def __str__(self):
        return f'Entrada - {str(self.pk)}'
    


class InflowItem(models.Model):
    inflow = models.ForeignKey(Inflow, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=0)    
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    class Meta:
        verbose_name = 'Item da Entrada'
        verbose_name_plural = 'Itens da Entrada'

    def __str__(self):
        return f'{self.product.title}'

