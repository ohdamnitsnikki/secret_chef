from django.shortcuts import render
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


def about(request):
    return render(request, 'about.html')


def post_form(request):
    return render(request, 'form.html')


def login(request):
    return render(request, 'login_signup.html')
