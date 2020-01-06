from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProjectsPage, name='projects_home'),

]