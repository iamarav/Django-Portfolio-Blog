from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePage, name='home_page'),
    path('about/', views.About, name='about_page'),
    path('contact/', views.ContactPage, name='contact_page'),
    path('testing/login/', views.LoginPage, name='login_page'),
    path('testing/logout/', views.LoginPage, name='logout_page'),
    path('testing/signup/', views.SignupPage, name='signup_page'),
]