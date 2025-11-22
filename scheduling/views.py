from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.decorators import customer_required
from .models import Appointment, Demo
from django.contrib import messages
from django.utils.dateparse import parse_datetime

@login_required
@customer_required
def book_appointment(request):
    if request.method == 'POST':
        date_str = request.POST.get('date')
        reason = request.POST.get('reason')
        date = parse_datetime(date_str)
        
        if date:
            Appointment.objects.create(customer=request.user, date=date, reason=reason)
            messages.success(request, "Appointment requested successfully!")
            return redirect('customer_dashboard')
        else:
            messages.error(request, "Invalid date format.")
            
    return render(request, 'scheduling/book_appointment.html')

@login_required
@customer_required
def book_demo(request):
    if request.method == 'POST':
        date_str = request.POST.get('date')
        product_interest = request.POST.get('product_interest')
        date = parse_datetime(date_str)
        
        if date:
            Demo.objects.create(customer=request.user, date=date, product_interest=product_interest)
            messages.success(request, "Demo requested successfully!")
            return redirect('customer_dashboard')
        else:
            messages.error(request, "Invalid date format.")

    return render(request, 'scheduling/book_demo.html')
