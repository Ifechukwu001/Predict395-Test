from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Post
from .forms import PostForm

post_queryset = Post.objects.all()


@login_required
def post_create(request):
    form = PostForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect("blog:detail", pk=form.instance.id)
    return render(request, "blog/post_create.html", {"form": form})


def post_list(request):
    posts = post_queryset.all()
    return render(request, "blog/post_list.html", {"posts": posts})


def post_detail(request, pk):
    posts = post_queryset.filter(pk=pk)
    if not posts.exists():
        return redirect("blog:list")

    post = posts.first()
    return render(request, "blog/post_detail.html", {"post": post})


@login_required
def post_update(request, pk):
    posts = post_queryset.filter(pk=pk, author=request.user)
    if not posts.exists():
        return redirect("blog:list")

    post = posts.first()
    form = PostForm(request.POST or None, instance=post)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("blog:detail", pk=post.id)
    return render(request, "blog/post_update.html", {"form": form})


@login_required
def post_delete(request, pk):
    posts = post_queryset.filter(pk=pk, author=request.user)
    if posts.exists():
        post = posts.first()
        post.delete()
    return redirect("blog:list")
