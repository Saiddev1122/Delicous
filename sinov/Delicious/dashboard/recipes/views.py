from django.shortcuts import redirect, render

from dashboard.recipes.forms import RecipeForm


def ctg_list(requests):
    return render(requests, 'dashboard/recipes/list.html')


def form(requests):
    ctg_form = RecipeForm()
    if requests.POST:
        forms = RecipeForm(requests.POST or None, requests.FILES or None)
        if forms.is_valid():
            forms.save()

    ctx = {
        'form': ctg_form
    }
    return render(requests, 'dashboard/recipes/form.html', ctx)


def detail(requests):
    return render(requests, 'dashboard/recipes/detail.html')


def search(requests):
    ctx = {}
    return render(requests, 'site/urls', ctx)
