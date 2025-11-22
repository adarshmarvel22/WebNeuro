from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.decorators import admin_required, staff_required, customer_required
from services.models import Order
from scheduling.models import Appointment, Demo
from communication.models import Message
from accounts.models import User

@login_required
@admin_required
def admin_dashboard(request):
    staff_members = User.objects.filter(role=User.Role.STAFF)
    recent_orders = Order.objects.all().order_by('-created_at')[:5]
    return render(request, 'dashboard/admin_dashboard.html', {
        'staff_members': staff_members,
        'recent_orders': recent_orders
    })

@login_required
@staff_required
def staff_dashboard(request):
    assigned_appointments = request.user.assigned_appointments.all()
    assigned_demos = request.user.assigned_demos.all()
    return render(request, 'dashboard/staff_dashboard.html', {
        'assigned_appointments': assigned_appointments,
        'assigned_demos': assigned_demos
    })

@login_required
@customer_required
def customer_dashboard(request):
    my_orders = request.user.orders.all()
    my_appointments = request.user.appointments.all()
    return render(request, 'dashboard/customer_dashboard.html', {
        'my_orders': my_orders,
        'my_appointments': my_appointments
    })
