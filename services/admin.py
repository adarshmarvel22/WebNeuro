from django.contrib import admin
from .models import Service, Order

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'created_at']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'service', 'status', 'created_at']
    list_filter = ['status', 'created_at']
