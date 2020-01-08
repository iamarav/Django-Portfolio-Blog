from django.urls import path

from . import views


urlpatterns = [
    path('', views.Blog, name="blog_home"),
    path('post/<int:post_id>', views.Single_Post_Page, name="single_post_page"),
    path('author/<int:author_id>', views.Author_Page, name="author_page"),

]