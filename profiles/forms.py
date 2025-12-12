from django.forms import ModelForm
from django import forms
from .models import Profile, Messages


class ProfileForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields["first_name"].widget.attrs.update(
            {
                "placeholder" : "first_name",
                
                
            }
        )
        
        self.fields["last_name"].widget.attrs.update(
            {
                "placeholder" : "last_name",
                
                
            }
        )
        
        self.fields["bio"].widget.attrs.update(
            {
                "placeholder" : "bio",
                
                
            }
        )
    class Meta:
        model = Profile
        fields = ["first_name","last_name","bio","profile_pic"]
        widgets = {
           "profile_pic" : forms.FileInput(),
        }
        
       

class MessageForm(ModelForm):
    def __init__(self , *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["text"].widget.attrs.update(
            {
                "placeholder" : "Send your message",
                "rows": 1,
                "id":"chat-input"
            }
        )
        
    class Meta:
        model = Messages
        fields = ["text"]
        widgets = {
            "text": forms.Textarea()
        }