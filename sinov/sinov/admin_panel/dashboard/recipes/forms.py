from django import forms

from dashboard.models import Recipes


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipes
        fields = "__all__"
