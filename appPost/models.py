from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.

class Post (models.Model): 
    fecha = models.DateTimeField(auto_now_add=True)
    titulo= models.CharField(max_length=20)
    texto = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='img-posts', default='')
    epigrafe = models.CharField(max_length=20, blank=True)




