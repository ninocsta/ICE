from django.db import models



class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    min_stock = models.IntegerField(default=0)
    weight = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return f'{self.title} {self.weight}kg'