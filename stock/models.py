from django.db import models
from products.models import Product


class Stock(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='stock')
    quantity = models.IntegerField(default=0)
    average_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Estoque'
        verbose_name_plural = 'Estoque'
        ordering = ['quantity']

    def __str__(self):
        return f'{self.product.title} {self.quantity}'