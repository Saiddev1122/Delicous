from django.contrib import admin

# Register your models here.
from dashboard.models import Category, Recipes, Ingredients

admin.site.register(Category)
admin.site.register(Recipes)
admin.site.register(Ingredients)
