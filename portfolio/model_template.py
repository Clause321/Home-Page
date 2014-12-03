'''
Created on Nov 28, 2014

@author: wyf
'''
from django.db import models

class ProjectLabel(models.Model):
    name = models.CharField(max_length=31)
    iflink = models.BooleanField(default = False)
    link = models.CharField(max_length=127, blank=True)

    def __str__(self):
        return self.name