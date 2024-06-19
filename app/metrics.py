from outflows.models import Outflow
from django.db.models import Sum



def get_sales_metrics(month):
    total_pending_sales = Outflow.objects.filter(status='P', delivery_date__month=month).count()
    total_delivered_sales = Outflow.objects.filter(status='E', delivery_date__month=month).count()
    profit = Outflow.objects.filter(status='E', delivery_date__month=month).aggregate(Sum('profit'))['profit__sum']



def get_monthly_profit():
    