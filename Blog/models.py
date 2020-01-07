from django.db import models
from django.utils import timezone as timezone
import datetime

from django.contrib.auth.models import User

# Create your models here.
        
class Categories(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Post(models.Model):
    title = models.CharField(max_length=250)
    featured_image = models.ImageField(upload_to='images/blog_images')
    excerpt =  models.CharField(max_length=2000)
    category = models.ForeignKey(Categories, on_delete=models.DO_NOTHING)
    content = models.TextField()
    date = models.DateField(default= timezone.now)
    time = models.TimeField(default= timezone.localtime().strftime('%H:%M:%S') )
    author = models.ForeignKey(
                            User,
                            on_delete= models.CASCADE
                        )
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete= models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment_time = datetime.datetime.now()
    comment = models.TextField() 
    date = models.DateField(default= timezone.now)
    time = models.TimeField(default= timezone.localtime().strftime('%H:%M:%S') )
    
    def __str__(self):
        return self.name
