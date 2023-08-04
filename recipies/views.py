from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.urls import reverse
from django.http import HttpResponseRedirect
from post.models import BlogPost


def about(request):
    return render(request, 'about.html')


def login(request):
    return render(request, 'login_signup.html')


def index(request):
    # Get all the posts with images from the database
    posts_with_images = BlogPost.objects.exclude(
        image='').order_by('-created_on')
    return render(
        request, 'index.html', {'posts_with_images': posts_with_images})
