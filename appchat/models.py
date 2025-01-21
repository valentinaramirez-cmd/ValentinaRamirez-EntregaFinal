from django.db import models

from appuser.models import User

# Create your models here.
class Mensaje (models.Model): 
    mensaje = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True, verbose_name='Enviado')

class ChatRoom (models.Model): 
    nombre = models.CharField(max_length=20)
    users  = models.ManyToManyField(User)
    mensajes = models.ManyToManyField(Mensaje, null=True, blank=True)

 