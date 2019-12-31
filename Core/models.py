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
