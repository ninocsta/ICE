from django.db import models
from clients.models import Client
from products.models import Product, PriceTable


class Outflow(models.Model):
    created_at = models.DateField(auto_now_add=True)
    delivery_date = models.DateField()
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    price_table = models.ForeignKey(PriceTable, on_delete=models.PROTECT)
    observation = models.TextField(blank=True, null=True)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(max_length=1, choices=[('P', 'Pendente'), ('E', 'Entregue')], default='P')
    profit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    class Meta:
        verbose_name = 'Saída'
        verbose_name_plural = 'Saídas'   

    def get_total_price(self):
        total_price = sum(item.total_price for item in self.items.all())
        return total_price
    
    def get_total_cost(self):
        total_cost = sum(item.product.stock.average_cost * item.quantity for item in self.items.all())
        total_cost += self.discount
        return total_cost

    def __str__(self):
        return f'Saída - {str(self.pk)}'


class OutflowItem(models.Model):
    outflow = models.ForeignKey(Outflow, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    class Meta:
        verbose_name = 'Item da Saída'
        verbose_name_plural = 'Itens da Saída'

    def __str__(self):
        return f'{self.product.title}' 