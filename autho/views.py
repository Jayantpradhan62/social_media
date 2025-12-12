from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView 
from django.contrib.auth import logout, login, authenticate



# Create your views here.

from .forms import RegisterForm, UserAuthenticationForm, ResetPasswordForm, ResetPasswordConfirmForm

# To Sign-up new users
class RegisterView(View):
    form_class  =   RegisterForm
    template = "autho/login.html"
    
    def get(self,request,*args, **kwargs):
        context = {"form2" : self.form_class(),"sign":True,"form":UserAuthenticationForm()}
        return render(request,self.template,context)
    
    def post(self,request,*args, **kwargs):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(request,username=username,password=password)
            login(request,user)
            return redirect(to="edit-profile")
        return render(request,self.template,{"form2":form,"sign":True,"form":UserAuthenticationForm()})


# Login user
class UserLoginView(LoginView):
    form_class = UserAuthenticationForm
    template_name = "autho/login.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form2"] = RegisterForm()
        context["sign"] = False
        return context


# Logout user
def LogoutView(request):
    logout(request)
    return redirect(to="user-login")

# Password-reset
class ResetPasswordView(PasswordResetView):
    template_name = "autho/password-reset.html"
    form_class = ResetPasswordForm
    success_url = reverse_lazy("reset-password-done")
    email_template_name = "autho/email_template.html"
   
    
class ResetPasswordDoneView(PasswordResetDoneView):
    template_name = "autho/password-reset-done.html"
    

class ResetPasswordConfirmView(PasswordResetConfirmView):
    template_name = "autho/password-reset-confirm.html"
    form_class = ResetPasswordConfirmForm
    success_url = reverse_lazy("reset-password-complete")


class ResetPasswordCompleteView(PasswordResetCompleteView):
    template_name = "autho/password-reset-complete.html"
    
    
    
    
    
    
    
        
