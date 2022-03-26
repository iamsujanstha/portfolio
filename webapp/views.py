from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

from django.conf import settings
from django.core.mail import send_mail

from webapp.forms import ContactForm
from .models import Project


# Create your views here.
def home(request):
    return render(request,'home.html')
    

def about(request):
    return render(request, 'about.html')

def portfolio(request):
    details = Project.objects.all()

    return render(request, 'portfolio.html', {'details':details})

def contact(request):
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('content')

            data = {
                'name':name,
                'email':email,
                'subject':subject,
                'message':message
            }

            message = '''
            {}

            Name: {}   From: {}
            '''.format(data['message'],data['name'],data['email'])
            
            send_mail(data['subject'],message,settings.EMAIL_HOST_USER,['tlsujank.co@gmail.com'],fail_silently=False)
            messages.success(request, 'Message sent successfully!!.')

        else:   
            form = ContactForm()
            messages.warning(request,'Please fill out the details!!')
    form = ContactForm()
    return render(request, 'contact.html', {'form':form})
