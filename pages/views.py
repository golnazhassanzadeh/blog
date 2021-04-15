from django.shortcuts import render
from posts.models import Post
from posts.forms import PostForm
from django.contrib import messages


# Create your views here.

def index_view(request):
    posts = Post.objects.all()
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = PostForm()
        messages.success(request,'saving successfully.')
    context = {
        'form':form,
        'posts': posts
    }
    return render(request, 'index.html', context)
