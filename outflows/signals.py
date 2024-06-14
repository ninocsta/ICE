from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Outflow, OutflowItem
from products.models import ProductPrice
from stock.models import Stock



@receiver(post_save, sender=OutflowItem)
def update_outflow(sender, instance, created, **kwargs):
    # Recalculate total_price for the OutflowItem, both when created and updated
    product_price = ProductPrice.objects.get(product=instance.product, price_table=instance.outflow.price_table)
    stock_item = Stock.objects.get(product=instance.product)
    if product_price:
        new_total_price = instance.quantity * product_price.price
        # Only update if total_price has actually changed to avoid unnecessary signal triggering
        if instance.total_price != new_total_price:
            instance.total_price = new_total_price
            instance.save(update_fields=['total_price'])
    else:
        raise ValueError('Produto sem preço cadastrado na tabela de preços selecionada!')    
   
    # Atualiza total_price do Outflow
    outflow = instance.outflow
    new_outflow_total_price = outflow.get_total_price()
    new_outflow_total_cost = outflow.get_total_cost()
    profit = new_outflow_total_price - new_outflow_total_cost
    # Atualiza se total_price ou total_cost mudou para evitar disparo desnecessário de signal
    if outflow.total_price != new_outflow_total_price or outflow.total_cost != new_outflow_total_cost:
        outflow.total_price = new_outflow_total_price
        outflow.total_cost = new_outflow_total_cost
        outflow.profit = profit
        outflow.save(update_fields=['total_price', 'total_cost', 'profit'])



@receiver(post_delete, sender=OutflowItem)
def update_outflow_on_delete(sender, instance, **kwargs):
     # Atualiza total_price e total_cost do Outflow
    outflow = instance.outflow
    new_outflow_total_price = outflow.get_total_price()
    new_outflow_total_cost = outflow.get_total_cost()
    profit = new_outflow_total_price - new_outflow_total_cost
    # Atualiza se total_price ou total_cost mudou para evitar disparo desnecessário de signal
    if outflow.total_price != new_outflow_total_price or outflow.total_cost != new_outflow_total_cost:
        outflow.total_price = new_outflow_total_price
        outflow.total_cost = new_outflow_total_cost
        outflow.profit = profit
        outflow.save(update_fields=['total_price', 'total_cost', 'profit'])


@receiver(post_save, sender=Outflow)
def update_stock_on_status_change(sender, instance, **kwargs):
    if instance.status == 'E':
        for item in instance.items.all():
            stock_item = Stock.objects.get(product=item.product)
            stock_item.quantity -= item.quantity
            stock_item.total_cost = stock_item.quantity * stock_item.average_cost
            stock_item.save(update_fields=['quantity', 'total_cost'])

# Atualiza total_price do Outflow
    outflow = instance
    new_outflow_total_price = outflow.get_total_price()
    new_outflow_total_cost = outflow.get_total_cost()
    profit = new_outflow_total_price - new_outflow_total_cost
    # Atualiza se total_price ou total_cost mudou para evitar disparo desnecessário de signal
    if outflow.total_price != new_outflow_total_price or outflow.total_cost != new_outflow_total_cost:
        outflow.total_price = new_outflow_total_price
        outflow.total_cost = new_outflow_total_cost
        outflow.profit = profit
        outflow.save(update_fields=['total_price', 'total_cost', 'profit'])