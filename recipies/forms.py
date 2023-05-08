from .models import Comment
from django import forms
from .models import Recipe


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class RecipeForm(forms.ModelForm):

    CATEGORY_CHOICES = (
        ('Breakfast', 'Breakfast'),
        ('Dinner', 'Dinner'),
        ('Dessert', 'Dessert')
    )

    title = forms.CharField(max_length=100, widget=forms.Textarea(attrs={'rows': 1, 'placeholder': 'Enter the title of the recipe', 'class': 'form-control'}))
    description = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Enter the description of the recipe', 'class': 'form-control'}))
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    photo = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Recipe
        fields = ('title', 'description', 'category', 'photo',)
