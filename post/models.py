from django.db import models
from django.contrib.auth.models import User

# Status on the posts
STATUS = ((0, "Draft"), (1, "Published"))


class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    TYPE_CHOICES = [
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
    ]
    type_of_dish = models.CharField(max_length=10, choices=TYPE_CHOICES)
    image = models.ImageField(upload_to='user_posts/')
    excerpt = models.TextField()
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        verbose_name = 'User Post'
        verbose_name_plural = 'User Posts'
        ordering = ["-created_on"]

    def __str__(self):
        return self.title
