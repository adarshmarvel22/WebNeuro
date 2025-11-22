from django.urls import path
from . import views

urlpatterns = [
    path('', views.service_list, name='service_list'),
    path('buy/<int:service_id>/', views.buy_service, name='buy_service'),
]
