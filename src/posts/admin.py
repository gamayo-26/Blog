from django.contrib import admin
from .models import Post, Comment, PostView, Like, User

# Register your models here.
admin.site.register(User)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(PostView)
admin.site.register(Like)
