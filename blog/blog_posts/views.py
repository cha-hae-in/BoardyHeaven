from django.shortcuts import render, redirect
from .models import Post, Comment

def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    comments = Comment.objects.filter(post=post).order_by('-created_at')
    return render(request, 'blog_posts/post_detail.html', {'post': post, 'comments': comments})

# Other views for creating, editing, and deleting comments as needed
