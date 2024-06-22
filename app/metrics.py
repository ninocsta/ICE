from outflows.models import Outflow, OutflowItem
from django.db.models import Sum, Value, DecimalField
from django.db.models.functions import Coalesce





def get_monthly_totals(year, month):    
    total_delivered_sales = Outflow.objects.filter(status='E', delivery_date__year=year, delivery_date__month=month).count()
    profit = Outflow.objects.filter(status='E', delivery_date__year=year, delivery_date__month=month).aggregate(
        total_profit=Coalesce(Sum('profit'), Value(0, output_field=DecimalField()))
    )['total_profit']
    total_month_cost = Outflow.objects.filter(status='E', delivery_date__year=year, delivery_date__month=month).aggregate(
        total_cost=Coalesce(Sum('total_cost'), Value(0, output_field=DecimalField()))
    )['total_cost']
    total_month_price = Outflow.objects.filter(status='E', delivery_date__year=year, delivery_date__month=month).aggregate(
        total_price=Coalesce(Sum('total_price'), Value(0, output_field=DecimalField()))
    )['total_price']

    return {
        'total_delivered_sales': total_delivered_sales,
        'profit': profit,
        'total_month_cost': total_month_cost,
        'total_month_price': total_month_price
    }


def get_product_sales(year, month):
    sales = OutflowItem.objects.filter(outflow__status='E', outflow__delivery_date__year=year, outflow__delivery_date__month=month)\
                               .values('product__title')\
                               .annotate(total_sales=Sum('quantity'))\
                               .order_by('-total_sales')[:6]

    product_titles = [sale['product__title'] for sale in sales]
    total_sales = [sale['total_sales'] for sale in sales]

    return product_titles, total_sales