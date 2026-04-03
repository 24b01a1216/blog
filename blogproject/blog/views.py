from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'blog/post_detail.html', {'post': post})

def home(request):
    return HttpResponse("Hello, your Django app is live on Railway 🚀")