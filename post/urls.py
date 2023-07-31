from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_blog_post, name='create_blog_post'),
    path('success/', views.blog_post_success, name='blog_post_success'),
    path('user_posts/', views.UserPostListView.as_view(), name='user_posts'),
    path('edit/<int:pk>/', views.edit_post_view, name='edit_post'),
]
