from datetime import datetime, time
from django import forms

from .models import Post


class PostForm (forms.ModelForm): 
    class Meta: 
        model = Post 
        fields =  ['titulo', 'epigrafe', 'imagen', 'texto']

class UpdatePostForm (forms.ModelForm): 
    user = None 
    
    class Meta: 
        model = Post 
        fields =  ['titulo', 'epigrafe', 'imagen', 'texto']
