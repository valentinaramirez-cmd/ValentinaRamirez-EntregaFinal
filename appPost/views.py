from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, DeleteView, ListView, UpdateView, TemplateView
from .forms import PostForm, UpdatePostForm
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here. 

class HomeView (LoginRequiredMixin, TemplateView): 
    template = './appPost/menu.html'
                
class CreatePostView (LoginRequiredMixin, CreateView): 
    model = Post
    form_class = PostForm
    template = './appPost/post_form.html'
    success_url = reverse_lazy('appPost:menu')

    def get_initial(self):
        initial = super().get_initial()
        initial['user'] = self.request.user
        return initial

class DeletePostView(LoginRequiredMixin, DeleteView): 
    model = Post 
    template_name= './auth/post_confirm_delete.html'
    success_url = reverse_lazy('appPost:menu')

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user)
    

class DetailPostView(LoginRequiredMixin, DetailView): 
    model = Post
    template_name = './appPost/detail_post.html'
    context_object_name = 'post'    

@login_required   
def create_post (request): 
    if request.method == 'POST' : 
        form = PostForm(request.POST, request.FILES) 

        if form.is_valid() :  
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('appPost:menu')
            
    else: 
        form = PostForm()

    return render(request, './appPost/post_form.html', {'form' : form})

@login_required
def editar_post (request, pk): 
    post = get_object_or_404(Post, id=pk)

    if post.user != request.user: 
        redirect('appPost:menu')

    if request.method == 'POST': 
        form = UpdatePostForm(request.POST, request.FILES, instance=post)

        if form.is_valid(): 
            form.save()
            return redirect('appPost:detail_post', pk=post.id)
    else: 
        form = UpdatePostForm(instance=post)
    
    return render (request, './appPost/editar_post.html', {'form' : form}) 




def get_posts(request): 
    posts = Post.objects.all()
    return render(request, './appPost/listar_posts.html', {'posts' : posts})


def get_all_user_posts(request, pk): 
    posts = Post.objects.filter(user__id=pk).values()
    return render(request, './appPost/listar_posts.html', {'posts' : posts})

