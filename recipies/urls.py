from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path("", views.PostList.as_view(), name="about"),
    path("", views.PostList.as_view(), name="post"),
    path("", views.PostList.as_view(), name="login/signup"),
]