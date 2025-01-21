from django.urls import path

from .views import CreatePostView, DeletePostView, DetailPostView, create_post, editar_post, get_all_user_posts, get_posts


app_name = 'appPost'

urlpatterns = [
    path('', get_posts, name="menu"), 
    path('postear/', create_post, name='postear'),
    path('delete_post/<int:pk>/', DeletePostView.as_view(), name='delete_post'), 
    path('ver_posts/<int:pk>/', get_all_user_posts, name='ver_posts'), 
    path('detail_post/<int:pk>/', DetailPostView.as_view(), name='detail_post'), 
    path('editar_post/<int:pk>/', editar_post, name='editar_post'), 
]

