from django import forms 
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User

from .models import Avatar

class UserCreationForm(UserCreationForm): 
    class Meta: 
        model = User 
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', 'email')
        
class UpdateUserForm (UserChangeForm):
    password = None
    class Meta: 
        model = User 
        fields = ('username', 'first_name', 'last_name', 'email')
           
class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']