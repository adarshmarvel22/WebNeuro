from django.urls import path
from . import views

urlpatterns = [
    path('appointment/', views.book_appointment, name='book_appointment'),
    path('demo/', views.book_demo, name='book_demo'),
]
