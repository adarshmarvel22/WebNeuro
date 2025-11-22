from django.shortcuts import render
from .models import Testimonial
from services.models import Service

def home(request):
    services = Service.objects.all()[:3]
    testimonials = Testimonial.objects.all()[:3]
    return render(request, 'core/home.html', {
        'services': services,
        'testimonials': testimonials
    })
