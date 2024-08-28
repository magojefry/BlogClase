from django.contrib import admin
from BlogClase_api.apps.blogs.models import Post, Category

# Register your models here.

admin.site.register(Post)
admin.site.register(Category)

