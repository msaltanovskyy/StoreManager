from django.db.models import Count
from django.shortcuts import render
from OrderManager.models import Order

def order_status_chart(request):
    statuses = Order.objects.values('status').annotate(count=Count('id'))
    labels = [status['status'] for status in statuses]
    data = [status['count'] for status in statuses]

    context = {
        'labels': labels,
        'data': data,
    }
    return render(request, 'charts/order_status_chart.html', context)
