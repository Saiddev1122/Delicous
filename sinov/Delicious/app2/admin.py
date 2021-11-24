from django.contrib import admin

# Register your models here.
from .models import Category, Ingredients, Recipes, Admin

admin.site.register(Category)
admin.site.register(Ingredients)
admin.site.register(Recipes)
admin.site.register(Admin)
