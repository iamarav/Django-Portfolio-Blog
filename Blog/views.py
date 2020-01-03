from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings 
from django.core.exceptions import *
from Blog.models import *

media_url = settings.MEDIA_URL
static = settings.STATIC_URL

blog_info = settings.BLOG_INFO

# Create your views here.
def Blog(request):
    blog_post_content = Post.objects.all().order_by('-id')

    return (render( request, 'template-blog-home.html', {'blog_content': blog_post_content, 'media_url': media_url, 'static_url': static, 'blog_info': blog_info }))
    # just to show some text on browser

def Single_Post_Page(request, post_id):
    try:
        post_object = Post.objects.get(id = post_id)
       # comments_object = Comment.objects.get(post_id = post_id)
        comments_object = {}
        
    except ObjectDoesNotExist:
        return 'Not found'
    return (render( request, 'template-blog-single-post.html', {'post': post_object, 'comments': comments_object, 'media_url': media_url, 'static_url': static, 'blog_info': blog_info }))

