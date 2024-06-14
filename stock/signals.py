from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Stock
from products.models import Product
from inflows.models import InflowItem

@receiver(post_save, sender=Product)
def create_stock(sender, instance, created, **kwargs):
    if created:
        Stock.objects.create(product=instance)
    


