from django.db import models
from django.utils import timezone as timezone
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Feedback(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(default="", blank=True, null=True, max_length=25)
    website = models.URLField(blank=True, null=True)
    city = models.CharField(blank=True, null=True, max_length=20)
    message = models.TextField()

    def __str__(self):
        return str(self.id)+": "+self.name

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20,null=True, blank=True)
    website = models.URLField(blank=True, null=True)
    subject = models.CharField(max_length=500, null=True, blank=True)
    message = models.TextField()
    date = models.DateField(default= timezone.now)
    time = models.TimeField(default= timezone.localtime().strftime('%H:%M:%S') )
    user_ip = models.CharField( max_length=25, default='' )

    def __str__(self):
        return str(self.name)+" ("+str(self.email)+"), "+str(self.date)+", "+str(self.time)
        
# class User(AbstractUser):
#    # is_active = models.BooleanField(default=False)
#     address = models.CharField(max_length=30, blank=True)