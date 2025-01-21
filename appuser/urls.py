from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import DeleteUserView, DetailUserView, LoginUserView, RegisterUserView, UpdateUserView, editar_avatar, logout, subir_avatar
from appPost.views import get_all_user_posts

app_name = 'appuser'

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'), 
    path('login/', LoginUserView.as_view(), name='login'),
    path('update_user/', UpdateUserView.as_view(), name='update_user'), 
    path('delete_user/', DeleteUserView.as_view(), name='delete_user'), 
    path('ver_perfil/', DetailUserView.as_view(), name='detail_user'), 

    path('logout/', logout, name='logout'),
    path('subir_avatar/', subir_avatar, name='subir_avatar'), 
    path('editar_avatar/', editar_avatar, name='editar_avatar'), 
    
    
] 

