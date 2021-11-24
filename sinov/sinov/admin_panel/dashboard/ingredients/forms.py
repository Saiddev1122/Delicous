from django import forms

from dashboard.models import Ingredients


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredients
        exclude = ["slug"]
        fields = "__all__"
