from django.shortcuts import render, redirect
from ..models import Recipes
from .forms import RecipeForm


def recipe_list(requests):
    all = Recipes.objects.all()
    ctx = {
        "all": all
    }
    return render(requests, 'dashboard/recipes/list.html', ctx)


def recipe_form(requests, pk=None):
    if pk:
        edit_one = Recipes.objects.get(pk=pk)
        form = RecipeForm(requests.POST or None,
                          requests.FILES or None,
                          instance=edit_one)
        if form.is_valid():
            form.save()
        ctx = {
            'edit_one': edit_one,
            'form': form
        }
    else:
        form = RecipeForm()
        if requests.POST:
            forms = RecipeForm(requests.POST or None,
                               requests.FILES or None)

            if forms.is_valid():
                forms.save()
        ctx = {'form': form,
               }

    return render(requests, 'dashboard/recipes/form.html', ctx)


def delete_recipe(requests, pk):
    root = Recipes.objects.get(pk=pk)
    root.delete()

    return redirect('ctg_list')


def recipe_detail(requests, pk):
    one = Recipes.objects.get(pk=pk)
    ctx = {'one': one}
    return render(requests, 'dashboard/recipes/detail.html', ctx)
