from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path("about/", views.about, name="about"),
    path("post/", views.post(), name="post"),
    path("login_signup/", views.login/signup(), name="login/signup"),
]
