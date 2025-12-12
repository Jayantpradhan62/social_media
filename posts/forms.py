from .models import Posts
from django import forms
from django.forms import ModelForm

class PostForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields["caption"].widget.attrs.update(
            {
                "placeholder" : "caption",
                
                
            }
        )
        
        self.fields["text"].widget.attrs.update(
            {
                "placeholder" : "about your post",
                
                
            }
        )
        
    
    class Meta:
        model = Posts
        fields = ["caption","text","post_image"]
        widgets = {
           "post_image" : forms.FileInput(),
        }
        