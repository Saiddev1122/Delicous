from django.shortcuts import render, redirect, HttpResponse

from app2.models import Admin
from . forms import AdminForms


def home(requests):
    if requests.POST:
        email = requests.POST.get('email')
        pas = requests.POST.get('pass')
        try:
            admin = Admin.objects.get(email=email)
            if admin and admin.password == pas and admin.is_activate == True:
                print('shetda ', admin)
                user = admin
                ctx = {
                    'user': user
                }
                return render(requests, 'dashboard/index.html')
            else:
                return redirect('login')
        except:
            return redirect('login')
    else:
        return render(requests, 'dashboard/index.html')


def login(requests):
    return render(requests, 'dashboard/register/login.html')


def register(requests):
    register_ = AdminForms()
    if requests.POST:
        email = requests.POST.get('email')
        pas = requests.POST.get('pass')
        try:
            admin = Admin.objects.get(email=email)
            if admin and admin.password == pas and admin.is_activate == True:
                print('shetda ', admin)
                user = admin
                ctx = {
                    'register': register_,
                    'user': user
                }
                return render(requests, 'dashboard/register.html')
            else:
                return redirect('register')
        except:
            return redirect('register')

    else:
        if requests.POST:
            email = requests.POST.get('email')
            pas = requests.POST.get('pass')
            try:
                admin = Admin.objects.get(email=email)
                if admin and admin.password == pas and admin.is_activate == True:
                    print('shetda ', admin)
                    user = admin
                    ctx = {
                        'register': register_,
                        'user': user
                    }
                    return render(requests, 'dashboard/register.html')
                else:
                    return redirect('register')
            except:
                return redirect('register')
    return render(requests, 'dashboard/register/register.html', {'register': register_})
