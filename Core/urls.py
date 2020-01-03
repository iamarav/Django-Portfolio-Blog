from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomePage),
    path('about/', views.About),
    path('contact/', views.ContactPage),
    path('blog/', include('Blog.urls')),
    path('jobs/', include('Jobs.urls')),
]