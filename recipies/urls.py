from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path("about/", views.about, name="about"),
    path("post_form/", views.post_form, name="post_form"),
    path("login/", views.login, name="login"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
