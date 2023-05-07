from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class RecipeForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    photo = forms.ImageField()
    CATEGORY_CHOICES = [
        ('1', 'Breakfast'),
        ('2', 'Dinner'),
        ('3', 'Dessert')
    ]

    category = forms.ChoiceField(choices=CATEGORY_CHOICES)
