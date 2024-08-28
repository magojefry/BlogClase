from django.shortcuts import render
from django.http import HttpResponse
from BlogClase_api.apps.blogs.models import *

# Create your views here.

def index(request):
    posts = Post.objects.all()
    categories = Category.objects.all()

    contxt = {
        'posts': posts,
        'cateries': categories
    }


    return render(request, "blogs/index.html",context=contxt)