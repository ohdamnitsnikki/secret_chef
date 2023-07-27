from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_blog_post, name='create_blog_post'),
    path('success/', views.blog_post_success, name='blog_post_success'),
]
