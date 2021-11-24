from django.shortcuts import render, redirect
from .models import Category, Recipes
from dashboard.category.forms import RecipesForm


# Create your views here.

def index(requests):
    ctgg = Category.objects.get(slug='milliy-taomlar')
    categoryy = Category.objects.get(slug='chet_taomlari')
    chet_taomlari = Recipes.objects.all().filter(category_id=categoryy.id)
    recipes = Recipes.objects.all().filter(category_id=ctgg.id)
    ctx = {
        'recipe': recipes,
        'chet': chet_taomlari

    }

    return render(requests, 'site/index.html', ctx)


def about(requests):
    return render(requests, 'site/about.html', {})


def contact(requests):
    return render(requests, 'site/contact.html', {})


def elements(requests):
    return render(requests, 'site/elements.html', {})


def search(requests, pk=None):
    category = Category.objects.get(slug='chet_taomlari')
    chet_taomlari = Recipes.objects.all().filter(category_id=category.id)

    if pk:
        one = Recipes.objects.get(pk=pk)

        ctx = {
            'one': one,
            'chet': chet_taomlari

        }
    else:
        recipess = Recipes.objects.all()
        if requests.GET.get:
            savol = requests.GET.get('search')
        else:
            savol = False
        all_list = []
        for i in recipess:
            if savol and savol in i.name:
                all_list.append(i)

        print("all_list: ", all_list)

        print("savol: ", savol)

        ctx = {
            "recipes": all_list,
            'rekdasan': recipess

        }

    return render(requests, 'site/receipe-post.html', ctx)
