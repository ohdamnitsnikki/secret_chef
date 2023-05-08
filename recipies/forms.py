from .models import Comment
from django import forms
from .models import Recipe
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit


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

    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.layout = Layout(
            Row(
                Column('title', css_class='form-group col-md-6 mb-3'),
                Column('category', css_class='form-group col-md-6 mb-3'),
                css_class='form-row'
            ),
            'description',
            'photo',
        )