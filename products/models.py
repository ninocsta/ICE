from django.db import models



class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    min_stock = models.IntegerField(default=0)
    weight = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return f'{self.title}'
    
    def has_price_table(self, price_table):
        return self.prices.filter(price_table=price_table).exists()



class PriceTable(models.Model):
    title = models.CharField(max_length=120)   
    description = models.TextField(blank=True, null=True) 

    class Meta:
        verbose_name = 'Tabela de Preços'
        verbose_name_plural = 'Tabelas de Preços'

    def __str__(self):  
        return self.title
    

class ProductPrice(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='prices')
    price_table = models.ForeignKey(PriceTable, on_delete=models.CASCADE, related_name='prices')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    class Meta:
        verbose_name = 'Preço do Produto'
        verbose_name_plural = 'Preços dos Produtos'
        unique_together = ['product', 'price_table']

    def __str__(self):
        return f'{self.product.weight}kg - R${self.price:.2f} - {self.price_table.title}'