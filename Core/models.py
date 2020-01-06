from django.db import models

# Create your models here.

class Feedback(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone_number = models.IntegerField(default="")
    website = models.URLField(blank=True, null=True)
    # city = models.TextChoices('Delhi', 'Mumbai', 'Mohali')
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