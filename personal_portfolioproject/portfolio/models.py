from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)
    
    def __str__(self):
        return f"{self.title} - {self.description[:50]}..."
        # or return self.title for just title