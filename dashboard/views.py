from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.decorators import admin_required, staff_required, customer_required
from services.models import Order
from scheduling.models import Appointment, Demo
from communication.models import Message
from accounts.models import User

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from accounts.forms import CustomUserCreationForm, CustomUserChangeForm

@login_required
@admin_required
def admin_dashboard(request):
    staff_members = User.objects.filter(role=User.Role.STAFF)
    all_orders = Order.objects.all().order_by('-created_at')
    all_appointments = Appointment.objects.all().order_by('-date')
    all_messages = Message.objects.all().order_by('-timestamp')
    
    return render(request, 'dashboard/admin_dashboard.html', {
        'staff_members': staff_members,
        'all_orders': all_orders,
        'all_appointments': all_appointments,
        'all_messages': all_messages
    })

@login_required
@admin_required
def add_staff(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = User.Role.STAFF
            user.save()
            messages.success(request, 'Staff member added successfully.')
            return redirect('admin_dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'dashboard/staff_form.html', {'form': form})

@login_required
@admin_required
def edit_staff(request, user_id):
    user = get_object_or_404(User, id=user_id, role=User.Role.STAFF)
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Staff member updated successfully.')
            return redirect('admin_dashboard')
    else:
        form = CustomUserChangeForm(instance=user)
    return render(request, 'dashboard/staff_form.html', {'form': form})

@login_required
@admin_required
def delete_staff(request, user_id):
    user = get_object_or_404(User, id=user_id, role=User.Role.STAFF)
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'Staff member deleted successfully.')
        return redirect('admin_dashboard')
    return render(request, 'dashboard/confirm_delete.html', {'object': user})

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
    my_demos = request.user.demos.all()
    return render(request, 'dashboard/customer_dashboard.html', {
        'orders': my_orders,
        'appointments': my_appointments,
        'demos': my_demos
    })
