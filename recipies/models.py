# My imports

from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Status on the posts
STATUS = ((0, "Draft"), (1, "Published"))


# Build up of post
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipie_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='recipie_like', blank=True)

# Order of post
    class Meta:
        ordering = ["-created_on"]

# Show number of likes
    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


# Build up for comments
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


# Build up for user posts
class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='recipes')

    def __str__(self):
        return self.name
