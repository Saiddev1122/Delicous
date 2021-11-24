from django import forms
from app2.models import Category, Recipes, Ingredients


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredients
        fields = '__all__'
