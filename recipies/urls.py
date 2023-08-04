from . import views
from django.urls import path

urlpatterns = [
    # path("", views.PostList.as_view(), name="home"),
    path('', views.index, name='index'),
    path("about/", views.about, name="about"),
    path("login/", views.login, name="login"),
]
