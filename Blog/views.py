from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings 
from django.core.exceptions import *
from Blog.models import *

from django.contrib.auth.models import User

media_url = settings.MEDIA_URL
static = settings.STATIC_URL

blog_info = settings.BLOG_INFO

# Create your views here.
def Blog(request):
    blog_post_content = Post.objects.all().order_by('-id')
    categories = Post.objects.order_by().values('category').distinct()
    
    return (render( request, 'blog/template-blog-home.html', {'blog_content': blog_post_content, 'categories': categories, 'media_url': media_url, 'static_url': static, 'blog_info': blog_info}))
    # just to show some text on browser

def Single_Post_Page(request, post_id):
    categories = Post.objects.order_by().values('category').distinct()
    try:
        post_object = Post.objects.get(id = post_id)
        author_name = get_author_name(post_object.author)
        try:
            comments_object = Comment.objects.filter(post_id = post_id)
        except ObjectDoesNotExist:
            comments_object = [{'comment': 'No Comments!'}]
    except ObjectDoesNotExist:
        return 'Not found'
    return (render( request, 'blog/template-blog-single-post.html', {'post': post_object,'categories': categories, 'comments': comments_object, 'media_url': media_url, 'static_url': static, 'blog_info': blog_info, 'author_name':author_name }))

def Author_Page (request, author_id):
    user_object = User.objects.get(id = author_id)
    user_posts = get_blog_posts(limit=3, user_id=author_id)
    passing_dictionary = {'author': user_object, 'user_posts' : user_posts, 'media_url': media_url, 'static_url': static }
    return (render( request, 'blog/template-author-info.html', passing_dictionary ))

def get_blog_posts(limit = 12, user_id = None):
    if user_id is not None:
        return Post.objects.filter(author = user_id)[:limit]
    return Post.objects.all().order_by('-id')[:limit]

def get_author_name(author_id):
    author_id =1
    user = User.objects.get(id=author_id)
    return user.username
