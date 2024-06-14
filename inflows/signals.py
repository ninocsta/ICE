from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import InflowItem, Inflow


@receiver(post_save, sender=InflowItem)
def update_total_cost(sender, instance, created, **kwargs):
    # Calculate the new total cost
    new_total_cost = instance.quantity * instance.unity_cost

    # Only save if the total cost has changed to prevent recursion
    if instance.total_cost != new_total_cost:
        instance.total_cost = new_total_cost
        # Use update_fields to only update the 'total_cost' field
        instance.save(update_fields=['total_cost'])

    # Update the total cost of the inflow
    instance.inflow.total_cost = instance.inflow.get_total_cost()
    instance.inflow.save(update_fields=['total_cost'])


@receiver(post_delete, sender=InflowItem)
def update_total_cost_on_delete(sender, instance, **kwargs):
    instance.inflow.total_cost = instance.inflow.get_total_cost()
    instance.inflow.save(update_fields=['total_cost'])


