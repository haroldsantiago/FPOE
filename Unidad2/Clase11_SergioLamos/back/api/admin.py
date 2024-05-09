from django.contrib import admin
from .models.post import Post
from .models.auto import Auto
admin.site.register(Post)
admin.site.register(Auto)
