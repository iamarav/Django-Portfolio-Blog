from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=250)
    summary =  models.CharField(max_length=200)
    images = models.ImageField(upload_to='images/projects/')
    category = models.CharField(max_length=300, default='Uncategorized')
    link = models.URLField(default='')
    def __str__(self):
        return self.title

class Sample(models.Model):
    name = models.CharField(max_length=1000)