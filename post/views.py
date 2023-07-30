from django.shortcuts import render, redirect
from .forms import BlogPostForm
from django.views import generic, View
from .models import BlogPost
from recipies.models import Post


# User posts view
class UserPostListView(generic.ListView):
    model = BlogPost
    queryset = BlogPost.objects.filter(status=1).order_by("-created_on")
    template_name = "post/user_posts.html"
    paginate_by = 6


# User post submit
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


# User posts success page
def blog_post_success(request):
    return render(request, 'post/blog_post_success.html')
