from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def JobsPage(request):
    return HttpResponse('Hello from Job Page')
    # just to show some text on browser
