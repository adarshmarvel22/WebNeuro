from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from .models import User
from django.views.generic import CreateView
from django.urls import reverse_lazy

class SignUpView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        # Default role is CUSTOMER, handled by model
        return super().form_valid(form)
