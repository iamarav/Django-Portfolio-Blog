from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePage, name='home_page'),
    path('about/', views.About, name='about_page'),
    path('contact/', views.ContactPage, name='contact_page'),
    path('dashboard/', views.DashboardPage, name='dashboard_page'),
    path('user/login/', views.LoginPage, name='login_page'),
    path('user/logout/', views.LoginPage, name='logout_page'),
    path('user/signup/', views.SignupPage, name='signup_page'),
    path('user/forgot_password/', views.LoginPage, name='forgot_password_page'),
]