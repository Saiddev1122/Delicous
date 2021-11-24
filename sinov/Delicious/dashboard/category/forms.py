from django import forms
from app2.models import Category, Recipes


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ["slug"]
        fields = "__all__"


class RecipesForm(forms.ModelForm):
    class Meta:
        model = Recipes
        exclude = ["slug"]
        fields = "__all__"
