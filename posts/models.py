from django.db import models
from django.contrib.auth.models import User

from cloudinary.models import CloudinaryField

# Create your models here.



class Posts(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name="posts")
    caption = models.CharField(max_length=20)
    text  = models.TextField(max_length=2000)
    likes = models.ManyToManyField(User,related_name="post_likes",blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    post_image = CloudinaryField("post_images")
    
    def __str__(self):
        return f"{self.caption}-{self.author.username}"
    
    def get_likes_count(self):
        return self.likes.count()
    
    def get_comments_count(self):
        return self.comments.count()
    
    



class Comments(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="comments")
    text = models.TextField(null=False,blank=False)
    post = models.ForeignKey(Posts,on_delete=models.CASCADE,related_name="comments",null=True)
    likes = models.ManyToManyField(User,related_name="comment_likes",blank=True)
    

    def __str__(self):
        return f"{self.user.username}-{self.post.caption}-{self.text}" 
    
    def get_likes_count(self):
        return self.likes.count()   

class Reply(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="reply_comments")
    text = models.TextField(null=False,blank=False)  
    comment = models.ForeignKey(Comments,on_delete=models.CASCADE,related_name="replies",null=True)
    replied_to = models.ForeignKey(User,on_delete=models.CASCADE,related_name="replied_to")
    likes = models.ManyToManyField(User,related_name="reply_likes",blank=True)
    

    
    def __str__(self):
        return f"{self.user.username}-{self.comment.text}-{self.text}"
    
    def get_likes_count(self):
        return self.likes.count()   

   

    
    
    
    
