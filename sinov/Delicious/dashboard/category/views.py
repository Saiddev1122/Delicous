from django.shortcuts import redirect, render

from dashboard.category.forms import CategoryForm, RecipesForm


def ctg_list(requests):
    return render(requests, 'dashboard/category/list.html')


def form(requests):
    ctg_form = CategoryForm()
    if requests.POST:
        forms = CategoryForm(requests.POST or None, requests.FILES or None)
        if forms.is_valid():
            forms.save()

    ctx = {
        'form': ctg_form
    }
    return render(requests, 'dashboard/category/form.html', ctx)


def detail(requests):
    return render(requests, 'dashboard/category/detail.html')
