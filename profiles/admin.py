from django.contrib import admin
from .models import Profile, Chats, Messages

# Register your models here.

admin.site.register(Profile)
admin.site.register(Chats)
admin.site.register(Messages)
