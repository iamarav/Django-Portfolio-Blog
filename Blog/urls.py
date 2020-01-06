from django.urls import path

from . import views


urlpatterns = [
    path('', views.Blog, name="blog_home"),
    path('post/<int:post_id>', views.Single_Post_Page),
    path('author/<int:author_id>', views.Author_Page),

]