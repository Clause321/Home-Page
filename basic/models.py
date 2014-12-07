from django.db import models
from portfolio.models import Project

# Create your models here.
    
class Slide(models.Model):
    project = models.ForeignKey(Project)
    active = models.BooleanField(default=True)
    keywords = models.CharField(max_length=127, default='')
    front_image = models.ImageField(upload_to='image/front/', default="")
    
    def __str__(self):
        return self.project.title