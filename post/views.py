from django.shortcuts import render, redirect, get_object_or_404
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


# Edit posts
def edit_post_view(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)

    # Check if the user is the author or an admin before allowing edits
    if not (request.user == post.author or request.user.is_staff):
        # Redirect to the post list if not authorized
        return redirect('user_post')  

    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            # Redirect to the user posts page after successful edit
            return redirect('user_posts')  
    else:
        form = BlogPostForm(instance=post)

    return render(request, 'post/edit_posts.html', {'form': form, 'post': post})
