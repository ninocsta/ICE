from django.shortcuts import render
from datetime import datetime
from django.http import JsonResponse
from . import metrics
import locale
from outflows.models import Outflow
from django.db.models import Sum






def dashboard(request):
    now = datetime.now()
    current_month = now.month
    current_year = now.year



    meses = [(current_year, current_month)]
    for i in range(1, 6):
        if current_month - i <= 0:
            meses.append((current_year - 1, 12 + (current_month - i)))
        else:
            meses.append((current_year, current_month - i))

    locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
    meses_formatados = [datetime(year, month, 1).strftime('%B').capitalize() for year, month in meses]

    lucros_mensais = []
    for year, month in meses:
        lucro_do_mes = Outflow.objects.filter(
            status='E',
            delivery_date__year=year,
            delivery_date__month=month
        ).aggregate(total_profit=Sum('profit'))['total_profit'] or 0
        lucros_mensais.append(float(lucro_do_mes))

    meses_formatados.reverse()
    lucros_mensais.reverse()

    total_pending_sales = Outflow.objects.filter(status='P').count()
    context = {
        'total_pending_sales': total_pending_sales,
        'meses_formatados': meses_formatados,
        'lucros_mensais': lucros_mensais,
    }
    return render(request, 'dashboard.html', context)


def get_data(request):
    data = request.GET.get('data')
    year, month = map(int, data.split('-'))
    monthly_totals = metrics.get_monthly_totals(year,month)
    product_sales = metrics.get_product_sales(year, month)
    data = {
        'monthly_totals': monthly_totals,
        'product_sales': product_sales
    }
    return JsonResponse({'data': data})