from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET
from django.views.generic import DetailView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from itertools import chain
import random
from django.db.models import Q


# Create your views here.

from .models import Profile, Chats, Messages
from django.contrib.auth.models import User

from .forms import ProfileForm, MessageForm
from posts.forms import PostForm


# Loads profile-page with GET method and post your posts with POST method
@login_required
def mainpage(request):
    context = {
            "profile" : request.user.profile,
            "form": PostForm(),
            
            }
    # Get your profile-page
    if request.method == "GET":
        return render(request,"profiles/index.html",context)
    
    # Post your posts
    elif request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        context["form"] = form
        if form.is_valid():
            post  = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect(to="main-page")
        
        return render(request,"profiles/index.html",context)


# Loads any user profile-page
class ProfilePage(DetailView):
    model = Profile
    template_name = "profiles/user.html"
    context_object_name = "profile"
    
    
    def dispatch(self, request, *args, **kwargs):
        
        if request.user.username == self.kwargs.get("username"):
            return redirect(to="main-page")
        return super().dispatch(request, *args, **kwargs)
    
    
    def get_object(self):
        username = self.kwargs.get("username")
        user = User.objects.get(username=username)
        return Profile.objects.get(user=user)
    
    def get_context_data(self, **kwargs):
        context  = super().get_context_data(**kwargs)
        context["does_follow"] = self.get_object().followers.filter(username=self.request.user.username).exists()
       
    
        return context
    
   

# Follow any user
@login_required
def follow(request,username):
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)
    if request.method == "POST":
        status = request.POST.get("status")
        
        if status == "follow":
            profile.followers.add(request.user)
            request.user.profile.following.add(profile.user)
        else:
            profile.followers.remove(request.user)
            request.user.profile.following.remove(profile.user)
        
        return redirect("user-page",username)
            

    
            
# Edit your user-profile
class EditProfile(View,LoginRequiredMixin):
    form_Class = ProfileForm
    template = "profiles/profile.html"
    
    def get(self,request,*args, **kwargs):
        context = {"form":self.form_Class(instance=self.request.user.profile)}
    
        return render(request,self.template,context)
    
    
    
    def post(self,request,*args, **kwargs):
        form = self.form_Class(request.POST,request.FILES,instance=self.request.user.profile)
        
        if form.is_valid():
            form.save()
            return redirect(to="main-page")
        
        else:
             return render(request,self.template,{"form":form})
        
    
# Search users    
@require_GET
def search_users(request):
    query = request.GET.get("q"," ")
    if query:
         users = User.objects.filter(username__icontains=query)
         results = []
         for user in users:
             results.append(
                 {
                     "username":user.username,
                     "profile_pic_url" : user.profile.profile_pic.url,
                     "profile_url" : reverse("user-page",args=[user.username])
                 }
             )
         return JsonResponse({"results":results})
    return JsonResponse({"results":[]})


# Search users in your chat page
@require_GET
def search_user_messages(request):
    query = request.GET.get("q")
    if query:
        users = User.objects.filter(username__icontains=query).exclude(id=request.user.id)
        results = []
        for user in users:
            chat = Chats.objects.filter(Q(first_user=request.user, second_user=user) | Q(first_user=user,second_user=request.user)).first()
            if not chat:
                chat =  Chats.objects.create(first_user=request.user,second_user=user)
            
            latest_message = chat.get_latest_message()[:30]
            
            results.append(
                {
                    "username":user.username,
                    "message_url": reverse("message-page",args=[user.username]),
                    "profile_pic_url" : user.profile.profile_pic.url,
                    "latest_message" : latest_message
                }
            )
        return JsonResponse({"results":results})
    return JsonResponse({"results":[]})
            
                

   

# Loads user's feed (posts of users who you follow)
@login_required
def homepage(request):
    context = {"user":request.user}
    posts = []
    following  = request.user.profile.following.all()
    for user in following:
        posts.append(user.posts.all())
        
    posts = sorted(chain(*posts),reverse=True,key=lambda obj:obj.created)
    context["posts"] = posts
            
    
    if request.method == "GET":
        return render(request,"profiles/home.html",context)


# Loads feed-page consisting of posts from all different users on the app
def feedpage(request):
    context = {}
    posts = []
    users = User.objects.all()
    for user in users:
        posts.append(user.posts.all())
    
    posts = sorted(chain(*posts),key=lambda x: random.random())
   
       
    context["posts"] = posts
    
    if request.method == "GET":
        return render(request,"profiles/feed.html",context)


# Loads another feed-page when you click on a post on Feed-page with the post at top and posts from another users below to scroll
@login_required
def fyp(request):
    context = {"user":request.user}
    posts = []
    users = User.objects.all()
    for user in users:
        posts.append(user.posts.all())
    
    posts = chain(*posts)
    
    if request.method == "GET":
        
        random_post_ids = request.session.get("random_post_ids")
        if random_post_ids:
            all_posts = {post.id: post for post in posts}
            random_posts = [all_posts[pid] for pid in random_post_ids if pid in all_posts]
            posts = random_posts
        else:
            posts = sorted(posts,key=lambda x: random.random())
                    
        
        top_post_id  = request.session.get("post")
        top_post = next((post for post in posts if str(post.id) == top_post_id), None)

        if top_post:
            posts.remove(top_post)
            posts.insert(0,top_post)
        context["posts"] = posts
        return render(request,"profiles/fyp.html",context)
    
        
    
    elif request.method == "POST":
        first_post_id = request.POST.get("first_post_id")
        request.session["post"] = first_post_id
        posts = sorted(posts,key=lambda x: random.random())
        random_post_ids = [post.id for post in posts]
        request.session["random_post_ids"] = random_post_ids

        
        
        return redirect(to="fyp")
    

        
# Loads your chat-page (GET method) and also creates chat with another user (POST method)
class ChatView(View,LoginRequiredMixin):
    template = "profiles/chat.html"
    form_class = MessageForm
    
    
    def dispatch(self, request, *args, **kwargs):
        
        if request.user.username  == self.kwargs.get("username") :
            return redirect(to="main-page")
        
        return super().dispatch(request, *args, **kwargs)
        
    def get(self,request,*args, **kwargs):
        username =  self.kwargs.get("username")
        user =  User.objects.get(username=username)
        context = {}
        chat = Chats.objects.filter(Q(first_user=request.user, second_user=user) | Q(first_user=user,second_user=request.user)).first()
        if not chat:
            chat =  Chats.objects.create(first_user=request.user,second_user=user)
        context["chat"] = chat
        context["form"] = self.form_class()
        context["user"] = user
        return render(request,self.template,context)
    
    def post(self,request,*args, **kwargs):
        context = {}
        username =  self.kwargs.get("username")
        user =  User.objects.get(username=username)
        chat = Chats.objects.filter(Q(first_user=request.user, second_user=user) | Q(first_user=user,second_user=request.user)).first()
        if not chat:
            chat =  Chats.objects.create(first_user=request.user,second_user=user)
        context["chat"] = chat
        context["user"] = user
        form = self.form_class(request.POST)
        context["form"] = form
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.reciever = user
            message.chat = chat
            message.save()
            return redirect("chat-page",user.username)
        return render(request,self.template,context)



# Loads your texts with a user (GET method) and also sends text to another user (POST method)
class MessageView(View,LoginRequiredMixin):
    template = "profiles/messages.html"
    form_class = MessageForm
    
    
    def dispatch(self, request, *args, **kwargs):
        
        if request.user.username  == self.kwargs.get("username") :
            return redirect(to="message-list-page")
        
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request,*args, **kwargs):
        context  = {}
        me = request.user
        username  = self.kwargs.get("username")
        chats = list(me.first_user.all())
        chats += me.second_user.all()

        chats = [ chat for chat in chats if len(chat.get_latest_message()) > 0 ]
        chats = sorted(chats,reverse=True,key=lambda obj: obj.get_latest_update())
        context["chats"] = chats
        if not username:
            context["user"] = False
            return render(request,self.template,context)

        user = User.objects.get(username=username)
        context["user"] = user
        user_chat = Chats.objects.filter(Q(first_user=request.user, second_user=user) | Q(first_user=user,second_user=request.user)).first()
        if not user_chat:
            user_chat =  Chats.objects.create(first_user=request.user,second_user=user)
        context["user_chat"] = user_chat
        context["form"] = self.form_class()
        return render(request,self.template,context)
    
    
    
    def post(self,request,*args, **kwargs):
        context = {}
        me =  request.user
        username  = self.kwargs.get("username")
        user = User.objects.get(username=username)
        chat = Chats.objects.filter(Q(first_user=request.user, second_user=user) | Q(first_user=user,second_user=request.user)).first()
        if not chat:
            chat =  Chats.objects.create(first_user=request.user,second_user=user)
        form = self.form_class(request.POST)

        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.reciever = user
            message.chat = chat
            message.save()
            return redirect("message-page",user.username)
        context["form"] = form
        context["user"] = user
        context["user_chat"] = chat
        chats = list(me.first_user.all())
        chats += me.second_user.all()
        chats = [ chat for chat in chats if len(chat.get_latest_message()) > 0 ]
        chats = sorted(chats,reverse=True,key=lambda obj: obj.get_latest_update())
        context["chats"] = chats
        return render(request,self.template,context)

    
    
        
        
            
           
       
            
        
        
        
    
    
 
        
        
    
        
    
    
    
    
    
