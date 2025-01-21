from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
from .models import Avatar
from .forms import UpdateUserForm, UserCreationForm
from django.contrib.auth.models import User
from appPost.models import Post 
from django.views.generic import DetailView, CreateView, DeleteView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from .forms import AvatarForm
from django.contrib.auth import logout

# Create your views here.

class LoginUserView (LoginView) : 
    template = './appuser/login_user.html '

class RegisterUserView(CreateView): 
    model = User 
    form_class= UserCreationForm
    template = './appuser/user_form.html'
    success_url = reverse_lazy('appuser:subir_avatar')
    
class UpdateUserView(LoginRequiredMixin, UpdateView): 
    model = User 
    form_class= UpdateUserForm
    template = './templates/appuser/edit_user.html' 
    success_url = reverse_lazy('appuser:detail_user')

    def get_object(self, queryset=None):
        return self.request.user
   

class DeleteUserView(LoginRequiredMixin, DeleteView): 
    model = User 
    template = './auth/user_confirm_delete.html'
    success_url = reverse_lazy('appuser:login')

    def get_object(self, queryset=None):
        return self.request.user

class DetailUserView(LoginRequiredMixin, DetailView): 
    model = User
    template_name = './appuser/detail_user.html'
    context_object_name = 'user'

    def get_object(self, queryset=None):
        return self.request.user
    

def logout(request):
    request.session.flush()
    return redirect('appuser:register')

@login_required
def subir_avatar(request):
    if request.method == 'POST':
        avatar = request.user.avatar 

        form = AvatarForm(request.POST, request.FILES, instance=avatar)
        if form.is_valid():
            form.save()
            return redirect('appPost:menu')
    else:
        form = AvatarForm()
    return render(request, './appuser/subir_avatar.html', {'form': form})

@login_required
def editar_avatar (request): 
    if request.method == 'POST': 
        try: 
            avatar = request.user.avatar
        except Avatar.DoesNotExist: 
            avatar = None 
        
        if avatar: 
            form = AvatarForm(request.POST, request.FILES, instance=avatar)
        else: 
            form = AvatarForm(instance=avatar)

        if form.is_valid(): 
            avatar_instance = form.save(commit=False)
            avatar_instance.user = request.user 
            avatar_instance.save()
            return redirect('appuser:detail_user')
    else: 
        if hasattr(request.user, 'avatar'):
            form = AvatarForm(instance=request.user.avatar)
        else : 
            form = AvatarForm()

    return render (request, './appuser/editar_avatar.html', {'form' : form}) 


@receiver(post_save, sender=User)
def create_avatar_for_user(sender, instance, created, **kwargs):
    if created:
        Avatar.objects.create(user=instance)

            