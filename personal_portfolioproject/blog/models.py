from django.db import models
from django.utils import timezone

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField(default=timezone.now)
    image = models.ImageField(blank=True, upload_to='blog/images/')
    
    
    def __str__(self):
        return self.title
        #f"{self.title} - {self.description[:50]}..."
        # or return self.title for just title