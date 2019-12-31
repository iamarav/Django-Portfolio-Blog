from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage),
    path('about/', views.About),
    path('contact/', views.ContactPage),
]