from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings

from .forms import *

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
            return HttpResponse('OK')
        else:
            print(form)
            return HttpResponse('NOT OK')
            ContactForm()

    return render( request, 'template-contact.html', {'static_url': static})
    # this renders the html page from template folder to frontent

def LoginPage(request):
    return render( request, 'accounts/template-login.html')
    #to make a login page