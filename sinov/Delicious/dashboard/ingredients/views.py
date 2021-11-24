from django.shortcuts import redirect, render

from dashboard.ingredients.forms import IngredientForm


def ctg_list(requests):
    return render(requests, 'dashboard/category/list.html')


def form(requests):
    ctg_form = IngredientForm()
    if requests.POST:
        forms = IngredientForm(requests.POST or None, requests.FILES or None)
        if forms.is_valid():
            forms.save()

    ctx = {
        'form': ctg_form
    }
    return render(requests, 'dashboard/ingredients/form.html', ctx)


def detail(requests):
    return render(requests, 'dashboard/ingredients/detail.html')
