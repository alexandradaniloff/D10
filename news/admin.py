from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Post, Category, Author, Comment


admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Comment)
admin.site.register(Post.categories.through)
