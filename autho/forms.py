from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm
from django import forms
from django.core.exceptions import ValidationError



class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields["username"].widget.attrs.update(
            {
                "placeholder" : "username",
                
                
            }
        )
        
        self.fields["email"].widget.attrs.update(
            {
                "placeholder" : "email",
                
                
            }
        )
        
        self.fields["password1"].widget.attrs.update(
            {
                "placeholder" : "create-password",
                
                
            }
        )
        
        self.fields["password2"].widget.attrs.update(
            {
                "placeholder" : "confirm-password",
                
                
            }
        )
    
    
    
    
    
    class meta:
        model = User
        fields = ["username","email","password1","password2"]
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email is already in use")
        return email
    
    def save(self, commit = True):
        user  = super().save(commit=False)
        user.email = self.cleaned_data.get("email")
        if commit:
            user.save()
        return user
    
    


class UserAuthenticationForm(AuthenticationForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields["username"].widget.attrs.update(
            {
                "placeholder": "username"
            }
        )
        
        self.fields["password"].widget.attrs.update(
            {
                "placeholder": "password"
            }
        )
    
    
    
   



class ResetPasswordForm(PasswordResetForm):
    
    def __init__(self, request = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields["email"].widget.attrs.update(
            {
                "placeholder": "e-mail"
            }
        )


class ResetPasswordConfirmForm(SetPasswordForm):
    def __init__(self, request = None,*args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields["new_password1"].widget.attrs.update(
            {
                "placeholder": "new password"
            }
        )
        
        self.fields["new_password2"].widget.attrs.update(
            {
                "placeholder": "confirm password"
            }
        )