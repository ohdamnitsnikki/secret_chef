
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path("", include("recipies.urls"), name="recipies-urls"),
    path("accounts/", include("allauth.urls")),
    path("post/", include("post.urls")),
]
