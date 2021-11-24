
from django import forms
from app2.models import Category, Recipes, Ingredients


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipes
        fields = '__all__'
