from django.contrib import admin
from .models import BlogPost
from django_summernote.admin import SummernoteModelAdmin


@admin.register(BlogPost)
class BlogPostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'type_of_dish', 'created_on')
    search_fields = ['title', 'excerpt', 'content']
    list_filter = ('type_of_dish', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_on',)
    summernote_fields = ('content',)
