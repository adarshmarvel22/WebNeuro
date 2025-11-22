from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Message
from accounts.models import User
from django.contrib import messages
from django.db.models import Q

@login_required
def inbox(request):
    messages_list = Message.objects.filter(recipient=request.user).order_by('-timestamp')
    return render(request, 'communication/inbox.html', {'messages': messages_list})

@login_required
def sent_messages(request):
    messages_list = Message.objects.filter(sender=request.user).order_by('-timestamp')
    return render(request, 'communication/sent_messages.html', {'messages': messages_list})

@login_required
def compose_message(request):
    if request.method == 'POST':
        recipient_username = request.POST.get('recipient')
        subject = request.POST.get('subject')
        body = request.POST.get('body')
        
        try:
            recipient = User.objects.get(username=recipient_username)
            Message.objects.create(sender=request.user, recipient=recipient, subject=subject, body=body)
            messages.success(request, "Message sent successfully!")
            return redirect('inbox')
        except User.DoesNotExist:
            messages.error(request, "User not found.")
            
    # For simplicity, allow sending to staff if customer, or anyone if staff/admin
    if request.user.role == User.Role.CUSTOMER:
        recipients = User.objects.filter(role__in=[User.Role.STAFF, User.Role.ADMIN])
    else:
        recipients = User.objects.exclude(id=request.user.id)
        
    return render(request, 'communication/compose_message.html', {'recipients': recipients})

@login_required
def view_message(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    if request.user != message.recipient and request.user != message.sender:
        messages.error(request, "You do not have permission to view this message.")
        return redirect('inbox')
        
    if request.user == message.recipient and not message.is_read:
        message.is_read = True
        message.save()
        
    return render(request, 'communication/view_message.html', {'message': message})
