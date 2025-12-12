from django.contrib import admin
from .models import Posts
from .models import Comments, Reply

# Register your models here.
admin.site.register(Posts)
admin.site.register(Comments)
admin.site.register(Reply)