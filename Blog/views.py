from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Blog(request):
    return HttpResponse('Hello from Blog Page')
    # just to show some text on browser
