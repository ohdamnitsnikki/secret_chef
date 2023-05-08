from . import views
from django.urls import path
from .forms import RecipeForm

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path("about/", views.about, name="about"),
    path("post_form/", views.post_form, name="post_form"),
    path("login/", views.login, name="login"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name="post_like"),
    path('submit_recipe/', views.submit_recipe, name='submit_recipe'),  
]
