from django.shortcuts import render, redirect
from .forms import BlogPostForm


def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog_post_success')
    else:
        form = BlogPostForm()

    return render(request, 'post/create_blog_post.html', {'form': form})


def blog_post_success(request):
    return render(request, 'post/blog_post_success.html')