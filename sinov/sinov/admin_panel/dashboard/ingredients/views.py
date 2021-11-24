from .forms import IngredientForm
from django.shortcuts import render, redirect
from dashboard.models import Ingredients


def ingedient_list(requests):
    all = Ingredients.objects.all()
    ctx = {
        "all": all
    }
    return render(requests, 'dashboard/ingredients/list.html', ctx)


def ingedient_form(requests, pk=None):
    if pk:
        edit_one = Ingredients.objects.get(pk=pk)
        form = IngredientForm(requests.POST or None,
                              requests.FILES or None,
                              instance=edit_one)
        if form.is_valid():
            form.save()
        ctx = {
            'edit_one': edit_one,
            'form': form
        }
    else:
        form = IngredientForm()
        if requests.POST:
            forms = IngredientForm(requests.POST or None,
                                   requests.FILES or None)

            if forms.is_valid():
                forms.save()
        ctx = {'form': form,
               }

    return render(requests, 'dashboard/ingredients/form.html', ctx)


def delete_ingedient(requests, pk):
    root = Ingredients.objects.get(pk=pk)
    print(root)
    root.delete()

    return redirect('ingredients_list')


def ingedient_detail(requests, pk):
    one = Ingredients.objects.get(pk=pk)
    ctx = {'one': one}
    return render(requests, 'dashboard/ingredients/detail.html', ctx)
