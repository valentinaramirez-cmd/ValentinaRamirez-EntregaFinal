from django.contrib import admin
from .models import ChatRoom, Mensaje


# Register your models here.

class MensajeAdmin (admin.ModelAdmin): 
    list_display = ('user', 'mensaje','fecha')

    list_filter = ('user', 'fecha')

class ChatRoomAdmin (admin.ModelAdmin): 
    list_display = ('nombre', 'users')

    list_filter = ('nombre')
    

admin.site.register(ChatRoom)
admin.site.register(Mensaje, MensajeAdmin)