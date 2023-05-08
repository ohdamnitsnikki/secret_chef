from .models import Comment
from django import forms
from .models import Recipe


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class RecipeForm(forms.ModelForm):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Name of dish'}),
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control is-invalid', 'placeholder': 'Please provide us with a clear description and measurements of your recipe.', 'required': True}),
        error_messages={'required': 'Please provide a description for your recipe.'},
    )
    category = forms.ChoiceField(
        choices=[
            ('', 'Choose category'),
            ('breakfast', 'Breakfast'),
            ('dinner', 'Dinner'),
            ('dessert', 'Dessert'),
        ],
        widget=forms.Select(attrs={'class': 'custom-select', 'required': True}),
        error_messages={'required': 'Please choose a category for your recipe.'},
    )
    photo = forms.ImageField(
        widget=forms.FileInput(attrs={'class': 'custom-file-input', 'id': 'validatedCustomFile', 'required': True}),
        error_messages={'required': 'Please upload a photo of your dish.'},
    )

    class Meta:
        model = Recipe
        fields = ('name', 'description', 'category', 'photo',)
