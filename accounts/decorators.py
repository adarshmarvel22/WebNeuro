from django.contrib.auth.decorators import user_passes_test
from .models import User

def admin_required(function=None):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.role == User.Role.ADMIN,
        login_url='login',
        redirect_field_name=None
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

def staff_required(function=None):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and (u.role == User.Role.STAFF or u.role == User.Role.ADMIN),
        login_url='login',
        redirect_field_name=None
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

def customer_required(function=None):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.role == User.Role.CUSTOMER,
        login_url='login',
        redirect_field_name=None
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
