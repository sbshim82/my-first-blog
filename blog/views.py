# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Post

from django.shortcuts import redirect
from .forms import PostForm

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            #return redirect('blog.views.post_detail', pk=post.pk)
            posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
            return render(request, 'blog/post_list.html', {'posts': posts})
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
