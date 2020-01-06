from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings

from .forms import *
from .models import *

# Define Global variables here
media_url = settings.MEDIA_URL
static = settings.STATIC_URL

def HomePage(request):
    return render( request, 'template-home.html')
    # just to show some text on browser

def About(request):
    return render( request, 'template-about.html', {'static_url': static})  
    # this renders the html page from template folder to frontent

def ContactPage(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            form_data = Contact(name = name, email = email, subject = subject, message = message)
            form_data.save()
            return HttpResponse('Form is submitted!')
        else:
            return HttpResponse('Please check your input and try again !')
            ContactForm()

    return render( request, 'template-contact.html', {'static_url': static})
    # this renders the html page from template folder to frontent

def LoginPage(request):
    return render( request, 'accounts/template-login.html')
    #to make a login page