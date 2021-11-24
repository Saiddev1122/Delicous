from .forms import CategoryForm
from django.shortcuts import render, redirect
from dashboard.models import Category


def ctg_list(requests):
    all = Category.objects.all()
    ctx = {
        "all": all
    }
    return render(requests, 'dashboard/ingredients/list.html', ctx)


def ctg_form(requests, pk=None):
    if pk:
        edit_one = Category.objects.get(pk=pk)
        form = Category(requests.POST or None,
                        requests.FILES or None,
                        instance=edit_one)
        if form.is_valid():
            form.save()
        ctx = {
            'edit_one': edit_one,
            'form': form
        }
    else:
        form = CategoryForm()
        if requests.POST:
            forms = CategoryForm(requests.POST or None,
                                 requests.FILES or None)
            if forms.is_valid():
                forms.save()
        ctx = {'form': form,
               }

    return render(requests, 'dashboard/ingredients/form.html', ctx)


def delete_ctg(requests, pk):
    root = Category.objects.get(pk=pk)
    root.delete()

    return redirect('ctg_list')


def ctg_detail(requests, pk):
    one = CategoryForm.objects.get(pk=pk)
    ctx = {'one': one}
    return render(requests, 'dashboard/ingredients/detail.html', ctx)
