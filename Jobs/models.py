from django.db import models

class Job(models.Model):
    images = models.ImageField(upload_to='images/')
    summary =  models.CharField(max_length=200)
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title

class Sample(models.Model):
    name = models.CharField(max_length=1000)