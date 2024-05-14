from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Post
from .forms import PostForm


@login_required
def post_create(request):
    form = PostForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = request.user
            form.save()
    return render(request, "blog/post_create.html", {"form": form})


def post_list(request):
    posts = Post.objects.all()
    return render(request, "blog/post_list.html", {"posts": posts})


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, "blog/post_detail.html", {"post": post})
