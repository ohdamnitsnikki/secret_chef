from .models import Comment
from django import forms
from .models import Recipe
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
