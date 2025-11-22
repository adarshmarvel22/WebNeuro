from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('staff/', views.staff_dashboard, name='staff_dashboard'),
    path('customer/', views.customer_dashboard, name='customer_dashboard'),
    path('staff/add/', views.add_staff, name='add_staff'),
    path('staff/edit/<int:user_id>/', views.edit_staff, name='edit_staff'),
    path('staff/delete/<int:user_id>/', views.delete_staff, name='delete_staff'),
]
