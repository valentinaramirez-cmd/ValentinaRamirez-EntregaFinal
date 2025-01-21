from django import forms

from .models import ChatRoom, Mensaje

class ChatRoomForm(forms.ModelForm): 
    class Meta: 
        model= ChatRoom 
        fields =  ['nombre']
        widgets = {
            'users' : forms.HiddenInput(), 
            'mensajes' : forms.HiddenInput(),

        }
    

class MensajeForm(forms.ModelForm): 
    class Meta: 
        model = Mensaje 
        fields =  "__all__"
        widgets = {
            'user' : forms.HiddenInput(),
            'fecha' : forms.HiddenInput(),
        }
        
    
 