from django.contrib import admin
from .models import Appointment, Demo

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['customer', 'staff', 'date', 'status']
    list_filter = ['status', 'date']

@admin.register(Demo)
class DemoAdmin(admin.ModelAdmin):
    list_display = ['customer', 'product_interest', 'date', 'status']
    list_filter = ['status', 'date']
