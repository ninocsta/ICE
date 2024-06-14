from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import InflowItem, Inflow
from stock.models import Stock


@receiver(post_save, sender=InflowItem)
def update_costs_and_stock(sender, instance, created, **kwargs):
    # Calculate the new total cost for InflowItem
    new_total_cost = instance.quantity * instance.product.cost

    # Only save if the total cost has changed to prevent recursion
    if instance.total_cost != new_total_cost:
        instance.total_cost = new_total_cost
        # Use update_fields to only update the 'total_cost' field
        instance.save(update_fields=['total_cost'])

    # Update the total cost of the inflow
    instance.inflow.total_cost = instance.inflow.get_total_cost()
    instance.inflow.save(update_fields=['total_cost'])

    # Update the product stock
    
    
    if created:  # This ensures the code runs only when a new InflowItem is created
        stock = Stock.objects.get(product=instance.product)
        stock.quantity += instance.quantity
        stock.total_cost += instance.total_cost
        if stock.quantity > 0:  # Prevent division by zero
            stock.average_cost = stock.total_cost / stock.quantity
        else:
            stock.average_cost = 0
        stock.save(update_fields=['quantity', 'total_cost', 'average_cost'])


@receiver(post_delete, sender=InflowItem)
def update_inflow_and_stock_on_delete(sender, instance, **kwargs):
    # Update the total cost of the inflow
    instance.inflow.total_cost = instance.inflow.get_total_cost()
    instance.inflow.save(update_fields=['total_cost'])

    # Update the stock related to the deleted InflowItem
    stock = Stock.objects.get(product=instance.product)
    stock.quantity -= instance.quantity
    stock.total_cost -= instance.total_cost
    if stock.quantity > 0:
        stock.average_cost = stock.total_cost / stock.quantity
    else:
        stock.average_cost = 0
    stock.save(update_fields=['quantity', 'total_cost', 'average_cost'])