from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from accounts.decorators import customer_required
from .models import Service, Order
from django.contrib import messages

def service_list(request):
    services = Service.objects.all()
    return render(request, 'services/service_list.html', {'services': services})

@login_required
@customer_required
def buy_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    if request.method == 'POST':
        Order.objects.create(customer=request.user, service=service)
        messages.success(request, f"Successfully purchased {service.title}!")
        return redirect('customer_dashboard')
    
    return render(request, 'services/order_confirm.html', {'service': service})
