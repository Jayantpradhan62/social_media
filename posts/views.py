from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse

# Create your views here.


from .models import Posts, Comments, Reply
from .models import Comments,Reply


# Loads a post
class PostView(DetailView):
    model = Posts
    context_object_name = "post"
    template_name = "posts/post.html"
    
    def get_object(self):
        id = self.kwargs.get("id")
        post = Posts.objects.get(id=id)
        return post
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        liked  = self.get_object().likes.filter(username=self.request.user.username).exists()
        context["liked"] = liked
        context["user"] = self.request.user
        return context
    


# Add comment on a post
@login_required
def add_comment(request,id):
    if request.method == "POST":
        post = Posts.objects.get(id=id)
        reply_comment = request.POST.get("comment-id")
        if reply_comment:
            comment = Comments.objects.get(id=reply_comment)
            text = request.POST.get("reply")
            user = request.POST.get("comment-author")
            comment_author = User.objects.get(username=user)
            reply = Reply.objects.create(user=request.user,text=text,comment=comment,replied_to=comment_author)
            return redirect(request.META.get("HTTP_REFERER",reverse("post",args=[id])))
        text = request.POST.get("user-comment")
        comment = Comments.objects.create(user=request.user,text=text,post=post)
        return redirect(request.META.get("HTTP_REFERER",reverse("post",args=[id])))
        


# Like/Unlike a post
@login_required
def add_like(request,id):
    post = Posts.objects.get(id=id)
    if request.method == "POST":
        action = request.POST.get("status")
        
        if action == "like":
            post.likes.add(request.user)
        else:
           post.likes.remove(request.user)
        
        
        return redirect(request.META.get("HTTP_REFERER",reverse("post",args=[id])))



# Like/Unlike a comment
@login_required
def comment_add_like(request,id,cmnt_id):
    comment = Comments.objects.get(id=cmnt_id)
    if request.method == "POST":
        action = request.POST.get("comment-status")
        
        if action == "like-comment":
            comment.likes.add(request.user)
        else:
           comment.likes.remove(request.user)
        
        return redirect(request.META.get("HTTP_REFERER",reverse("post",args=[id])))



# Reply to a comment on post
@login_required
def reply_add_like(request,id,reply_id):
    reply = Reply.objects.get(id=reply_id)
    if request.method == "POST":
        action = request.POST.get("reply-status")
        
        if action == "like-reply":
            reply.likes.add(request.user)
        else:
           reply.likes.remove(request.user)
        
        return redirect(request.META.get("HTTP_REFERER",reverse("post",args=[id])))



    
    
              
        
    
    