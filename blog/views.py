from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    b = Post.objects.all()
    print(b)
    return render(request,'blog/index.html',{'b':b})

def about(request):
    return render(request,'blog/about.html')

def contact(request):
    return render(request,'blog/contact.html')

def post(request,id):
    post = Post.objects.filter(post_id=id)[0]
    print(post)
    return render(request,'blog/post.html',{'post':post})