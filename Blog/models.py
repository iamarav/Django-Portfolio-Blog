from django.db import models
from django.utils import timezone as timezone
import datetime

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=250)
    featured_image = models.ImageField(upload_to='images/blog_images')
    excerpt =  models.CharField(max_length=2000)
    category = models.CharField(max_length=200, default="Uncategorized")
    content = models.TextField()
    date = models.DateField(default= timezone.now)
    time = models.TimeField(default= timezone.localtime().strftime('%H:%M:%S') )
   # author = models.ForeignKey(admin.users, default=1, verbose_name="Category", on_delete=models.SET_DEFAULT)
    author = models.CharField(max_length=50, default=1)
    def __str__(self):
        return self.title

class Comment(models.Model):
    post_id = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment_time = datetime.datetime.now()
    comment = models.TextField() 
    date = models.DateField(default= timezone.now)
    time = models.TimeField(default= timezone.localtime().strftime('%H:%M:%S') )
    # post_id = models.ForeignKey(Posts.id)

    def __str__(self):
        return self.name