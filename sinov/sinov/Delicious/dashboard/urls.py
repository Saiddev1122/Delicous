from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from . import views

urlpatterns = [
    path('ctg/', include('dashboard.category.urls'), name='dashboard-category'),
    path('ingredients/', include('dashboard.ingredients.urls'), name='dashboard-ingredients '),
    path('recipes/', include('dashboard.recipes.urls'), name='dashboard-ingredients'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('index/', views.home, name='dashboard_index'),
]
