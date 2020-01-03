from django.http import HttpResponse
from django.shortcuts import render

def HomePage(request):
    return render( request, 'template-home.html')
    # just to show some text on browser

def About(request):
    return render( request, 'template-about.html')  
    # this renders the html page from template folder to frontent

def ContactPage(request):
    return render( request, 'template-contact.html', {'variable': 'value'})
    # this renders the html page from template folder to frontent

def LoginPage(request):
    return render( request, 'accounts/template-login.html')
    #to make a login page