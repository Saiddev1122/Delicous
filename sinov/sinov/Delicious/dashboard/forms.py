from django import forms
from app2.models import Admin


class AdminForms(forms.ModelForm):
    class Meta:
        model = Admin
        fields = '__all__'

