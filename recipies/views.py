from django.shortcuts import render
from django.views import genericfrom
from .models import Post


# Display posts for users
class PostList(generic.ListViews):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6
