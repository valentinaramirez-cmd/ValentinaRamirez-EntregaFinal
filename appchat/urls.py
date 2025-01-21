from django.urls import path

from .views import create_chatroom, enterRoom, chatRoom, ver_rooms

app_name = 'appchat'

urlpatterns = [
    path('room/<int:pk>', chatRoom, name='chatroom'), 
    path('enter_room/<int:pk>', enterRoom, name='enterRoom'),
    path('ver_rooms/', ver_rooms, name='ver_rooms'),
    path('create_chatroom/', create_chatroom, name='create_chatroom') 
    
]