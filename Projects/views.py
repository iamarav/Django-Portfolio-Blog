from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from Projects.models import *

static = settings.STATIC_URL
media = settings.MEDIA_URL
site_info = settings.SITE_INFO

# Create your views here.
def ProjectsPage(request):
    projects = Project.objects.all()
    render_dictionary = { 'static_url': static, 'projects': projects, 'media_url': media, 'site_info':site_info }
    return render( request, 'projects/template-projects-home.html', render_dictionary)
    # just to show some text on browser
