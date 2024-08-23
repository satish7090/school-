from django.db import models

# Create your models here.

class schoollist(models.Model):
    school_name= models.CharField(max_length=100)
    email=models.CharField(max_length=40)
    phone=models.CharField(max_length=14,unique=True)
    address=models.CharField(max_length=30)
    
    def __str__(self):
        return self.title

