from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from datetime import datetime
from django.utils.timezone import make_aware

from cloudinary.models import CloudinaryField

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    bio = models.CharField(max_length=50)
    profile_pic = CloudinaryField('profile_pic',default='default_cfcdht', null=True, blank= True)
    email = models.EmailField(max_length=200,blank=True)
    following = models.ManyToManyField(User,related_name="following",blank=True)
    followers = models.ManyToManyField(User,related_name="followers",blank=True)
    
    

    
    def __str__(self):
        return self.user.username
    
    def get_followers(self):
        return self.followers.count()
    
    def get_following(self):
        return self.following.count()
    
    def get_post_count(self):
        return self.user.posts.count()
    

        

class Chats(models.Model):
    first_user  = models.ForeignKey(User,related_name="first_user",on_delete=models.CASCADE)
    second_user =  models.ForeignKey(User,related_name="second_user",on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated =models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f"{self.first_user}-{self.second_user}"
    
    def get_latest_message(self):
        latest_message = self.messages.last()
        if latest_message:
             return latest_message.text
        return ""
    
    def get_latest_update(self):
        latest_message = self.messages.last()
        if latest_message:
            return latest_message.created
        return make_aware(datetime.min)
        
       

       
    

    
class Messages(models.Model):
    chat = models.ForeignKey(Chats,related_name="messages",on_delete=models.CASCADE)
    sender = models.ForeignKey(User,related_name="message_sender",on_delete=models.CASCADE)
    reciever = models.ForeignKey(User,related_name="message_reciever",on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=2000)
    
    
    class Meta:
        ordering = ["created"]
    
    
    def __str__(self):
        return f"{self.sender}-{self.reciever}"
